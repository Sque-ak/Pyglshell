import pyglet, os

from classes.windows.c_window import Window, WindowsManager
from const import STYLES
from utils.types.t_colors import RGB,RGBA
from utils.types.t_vectors import SVEC2, VEC2

class ComponentWindow(Window): 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._batch = None
        self._background = None
        self._background_color:RGB = STYLES.COLOR_BALANCE.value.BACKGROUND.value
        self._title_background_color:RGB = STYLES.COLOR_BALANCE.value.BACKGROUND.value + 5
        self._title_color:RGB|RGBA = STYLES.COLOR_BALANCE.value.ON_BACKGROUND.value
        self._title:str = self.name
        self._title_height:float = 24
        self._title_icon = STYLES.ICONS.value.NOICON.value.icon
        self._title_icon.width = STYLES.ICONS.value.NOICON.value.size.width
        self._title_icon.height = STYLES.ICONS.value.NOICON.value.size.height
        self._show_title:bool = False

    @property
    def title(self) -> str:
        return self._title
    
    @title.setter
    def title(self, title:str, without_name:bool = False) -> None:
        self._title = f'{self.name} {title}' if not without_name else title

    @property
    def show_title(self) -> bool:
        return self._show_title
    
    @show_title.setter
    def show_title(self, show_title:bool) -> None:
        self._show_title = show_title

    @property
    def title_height(self) -> float:
        return self._title_height
    
    @title_height.setter
    def title_height(self, title_height:float) -> None:
        self._title_height = title_height

    @property
    def title_color(self) -> RGB|RGBA:
        return self._title_color
    
    @title_color.setter
    def title_color(self, title_color:RGB|RGBA) -> None:
        self._title_color = title_color

    @property
    def title_background_color(self) -> RGB|RGBA:
        return self._title_background_color
    
    @title_background_color.setter
    def title_background_color(self, title_background_color:RGB|RGBA) -> None:
        self._title_background_color = title_background_color

    @property
    def title_icon(self):
        return self._title_icon
    
    @ title_icon.setter
    def title_icon(self, title_icon_path:str|pyglet.image.AbstractImage) -> None:
        if isinstance(title_icon_path, str):
            if os.path.isfile(title_icon_path):
                self._title_icon = pyglet.resource.image(title_icon_path)
        else:
            self._title_icon = title_icon_path
        #TODO else: SendLog('File not existd')!!!

    @property
    def background_color(self) -> RGB|RGBA:
        return self._background_color
    
    @background_color.setter
    def background_color(self, color:RGB|RGBA) -> None:
        self._background_color = color

    def on_draw(self) -> None: 
        self._batch.draw()

    def on_redraw(self) -> None:
        self._background = pyglet.shapes.Rectangle(self.position.x, self.position.y, self.size.width, self.size.height, color=self.background_color.__repr__(), batch=self._batch)
        if self.show_title:
            self.title_background = pyglet.shapes.Rectangle(self.position.x, self.position.y + self.size.height - self.title_height, self.size.width, self.title_height, color=self.title_background_color.__repr__(), batch=self._batch)
            self.title_label = pyglet.text.Label(self.title + ' Size: ' +str((self.size.x, self.size.y)) + ' Position: ' + str((self.position.x, self.position.y)), font_name=STYLES.FONT.value, color=self.title_color.__repr__(), font_size=STYLES.FONT_SIZE.value, x=self.position.x + 10 + self.title_icon.width, y=self.position.y + self.size.height - self.title_height + (self.title_height - STYLES.FONT_SIZE.value + 3) / 2, batch=self._batch)
            self.title_label_icon = pyglet.sprite.Sprite(img=self.title_icon, x=self.position.x + 3, y=self.position.y + self.size.height - self.title_height + (self.title_height - self.title_icon.width) / 2, batch=self._batch)

    def get_vertix(self) -> tuple[(VEC2, VEC2, VEC2, VEC2)]:
        ''' left-top - left-bottom - right-top - right-bottom''' 
        return (VEC2(self.position.x, self.position.y), VEC2(self.position.x, self.position.y + self.size.y), VEC2(self.position.x + self.size.x, self.position.y), VEC2(self.position.x + self.size.x, self.position.y + self.size.y))

    def on_init(self) -> None: 
        self._batch = pyglet.graphics.Batch()
        self.on_redraw()

    def on_resize(self, width:int = 0, height:int = 0) -> None:
        self.on_redraw()

    def run(self) -> None:
        pass


class ComponentWindowsManager(WindowsManager):    

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._window = pyglet.window.Window(*args, **kwargs)
        self._size:SVEC2 = SVEC2(0,0)
        self._event_loop = pyglet.app.event_loop

    def update_size(self) -> None:
        self.size = SVEC2(self.window.display.get_screens()[0].width, self.window.display.get_screens()[0].height)

    def on_draw(self):
        """
        The Window dispatches an on_draw() event whenever it's readt to redraw its contents.
        """
        self._window.clear()
        for child in self.children.values():
            child['window'].on_draw() # Draw all children of the Window

    def on_init(self) -> None:
        self.update_size()
        self.layout.do_layout()

        for child in self.children.values():
            child['window'].on_init() # Init all children of the Window
            
        # Set function on event
        self.on_draw = self._window.event(self.on_draw) 
        self.on_resize = self._window.event(self.on_resize)

    def on_resize(self, width:int = 0, height:int = 0):
        self.size = SVEC2(width, height)
        self.layout.do_layout()

        for child in self.children.values():
            child['window'].on_resize(width, height)

    def run(self, interval: float | None = 1 / 60) -> None:

        self.clock = pyglet.clock.get_default()
        self._event_loop._interval = interval
        
        if interval is None:
            pass # User must call Window.draw() themselves.
        if interval == 0:
            self.clock.schedule(self._event_loop._redraw_windows)
        else:
            self.clock.schedule_interval(self._event_loop._redraw_windows, interval)

        self._event_loop.has_exit = False

        from pyglet.window import Window
        Window._enable_event_queue = False

        # Dispatch pending events
        for window in pyglet.app.windows:
            window.switch_to()
            window.dispatch_pending_events()
            
        self._event_loop.dispatch_event('on_enter')
        platform_event_loop = pyglet.app.platform_event_loop
        platform_event_loop.start()
        
        self._event_loop.is_running = True

        while not self._event_loop.has_exit:
            timeout = self._event_loop.idle()
            for child in self.children.values():
                child['window'].run() # Run all children of the Window
            platform_event_loop.step(timeout)

        self._event_loop.is_running = False
        self._event_loop.dispatch_event('on_exit')
        platform_event_loop.stop()

    def create_window(self, *args, **kwargs) -> ComponentWindow:
        window = ComponentWindow( *args, **kwargs)
        self.add(window)
        return window

    def destroy_window(self, name:str) -> None: ...