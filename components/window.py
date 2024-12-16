import pyglet

from classes.windows.c_window import Window, WindowsManager
from classes.windows.c_layout import Layout
from const import COLOR_BALANCE
from pyglshell_types.t_colors import RGB
from pyglshell_types.t_vectors import SVEC2, VEC2

class ComponentWindow(Window): 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._batch = None
        self._background = None
        self._background_color = COLOR_BALANCE['background']

    @property
    def background_color(self) -> RGB:
        return self._background_color
    
    @background_color.setter
    def background_color(self, rgb:RGB) -> None:
        self._background_color = rgb

    def on_draw(self) -> None: 
        self._batch.draw()

    def on_redraw(self) -> None:
        self._background = pyglet.shapes.Rectangle(self.position.x, self.position.y, self.size.width, self.size.height, color=self._background_color.__repr__(), batch=self._batch)

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