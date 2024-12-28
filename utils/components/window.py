import os
from pyglet import resource, window, app, clock

from pyglet.graphics import Batch
from pyglet.shapes import Rectangle
from pyglet.text import Label
from pyglet.sprite import Sprite
from pyglet.image import AbstractImage

from classes.windows.c_window import Window, WindowsManager
from utils.types.t_colors import RGB,RGBA
from utils.types.t_vectors import SVEC2, VEC2

from pydantic import field_validator
from const import STYLES

class ComponentWindow(Window): 
    '''
    The `ComponentWindow` class is a custom window implementation that extends the `Window` class. It provides a set of properties and methods to manage the appearance and behavior of a window, including:

    - `batch`: A `Batch` object used for drawing the window's contents.
    - `background`: A `Rectangle` object representing the window's background.
    - `background_color`: The RGB color of the window's background.
    - `title_background_color`: The RGB color of the window's title bar background.
    - `title_color`: The RGB or RGBA color of the window's title text.
    - `title`: The title of the window, or the name of the window if not set.
    - `title_height`: The height of the window's title bar.
    - `title_icon`: An `AbstractImage` object representing the icon to be displayed in the title bar.
    - `show_title`: A boolean indicating whether the title bar should be displayed.

    The class also includes methods for drawing the window's contents (`on_draw`), redrawing the window when it is resized (`on_redraw`), initializing the window (`on_init`), and handling window resizing events (`on_resize`). The `run` method is included but does not contain any implementation.
    '''
    batch:Batch = None
    background:Rectangle = None
    background_color:RGB = STYLES.COLOR_BALANCE.value.BACKGROUND.value
    title_background_color:RGB = STYLES.COLOR_BALANCE.value.BACKGROUND.value + 5
    title_color:RGB|RGBA = STYLES.COLOR_BALANCE.value.ON_BACKGROUND.value
    title:str = None
    title_height:float = 24
    title_icon:AbstractImage = STYLES.ICONS.value.NOICON.value.icon
    title_icon.width = STYLES.ICONS.value.NOICON.value.size.width
    title_icon.height = STYLES.ICONS.value.NOICON.value.size.height 
    show_title:bool = False

    title_background: Rectangle = None
    title_label: Label = None
    title_label_icon: Sprite = None

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **data):
        super().__init__(**data)
        if self.title is None:
            self.title = self.name
 
    @field_validator('title_icon', mode='before')
    def validate_title_icon(cls, value:str|AbstractImage) -> None:
        if isinstance(value, str):
            if os.path.isfile(value):
                return resource.image(value)
            else:
                raise ValueError(f"File does not exist: {value}")
        elif isinstance(value, AbstractImage):
            return value
        else:
            raise TypeError("title_icon must be a string path or AbstractImage")

    def on_draw(self) -> None: 
        self.batch.draw()

    def on_redraw(self) -> None:
        self.background = Rectangle(self.position.x, 
                                    self.position.y, 
                                    self.size.width, 
                                    self.size.height, 
                                    color=self.background_color.__repr__(), 
                                    batch=self.batch)
        if self.show_title:
            self.title_background = Rectangle(self.position.x, 
                        self.position.y + self.size.height - self.title_height, 
                        self.size.width, self.title_height, 
                        color=self.title_background_color.__repr__(), 
                        batch=self.batch)
                
            self.title_label = Label(self.title + ' Size: ' +str((self.size.x, self.size.y)) + ' Position: ' + str((self.position.x, self.position.y)), 
                    font_name=STYLES.FONT.value, 
                    color=self.title_color.__repr__(), 
                    font_size=STYLES.FONT_SIZE.value, 
                    x=self.position.x + 10 + self.title_icon.width, 
                    y=self.position.y + self.size.height - self.title_height + (self.title_height - STYLES.FONT_SIZE.value + 3) / 2,
                    batch=self.batch)
                
            self.title_label_icon = Sprite(img=self.title_icon, 
                    x=self.position.x + 3, 
                    y=self.position.y + self.size.height - self.title_height + (self.title_height - self.title_icon.width) / 2, 
                    batch=self.batch)

    def on_init(self) -> None: 
        if self.batch == None:
            self.batch = Batch()
        self.on_redraw()

    def on_resize(self, width:int = 0, height:int = 0) -> None:
        self.on_redraw()

    def run(self) -> None:
        pass


class ComponentWindowsManager(WindowsManager):    
    '''
        The `ComponentWindowsManager` class is responsible for managing a collection of `ComponentWindow` instances. 
        It provides methods for creating, updating, and destroying windows, as well as handling events such as drawing and resizing. 
        The class also manages the overall event loop and clock for the application.
    '''
    def __init__(self, **data):
        super().__init__(**data)
        if self.window == None:
            self.window = window.Window(**data)
        
    class Config:
        arbitrary_types_allowed = True

    size:SVEC2 = SVEC2(0,0)
    event_loop:app.EventLoop = app.event_loop

    def update_size(self) -> None:
        self.size = SVEC2(self.window.display.get_screens()[0].width, self.window.display.get_screens()[0].height)

    def on_draw(self):
        """
        The Window dispatches an on_draw() event whenever it's readt to redraw its contents.
        """
        self.window.clear()
        for child in self.children.values():
            child['window'].on_draw() # Draw all children of the Window

    def on_init(self) -> None:
        self.update_size()
        self.layout.do_layout()

        for child in self.children.values():
            child['window'].on_init() # Init all children of the Window
            
        # Set function on event
        self.window.event(self.on_draw) 
        self.window.event(self.on_resize)

    def on_resize(self, width:int = 0, height:int = 0) -> None:
        self.size = SVEC2(width, height)
        self.layout.do_layout()

        for child in self.children.values():
            child['window'].on_resize(width, height)

    def run(self, interval: float | None = 1 / 60) -> None:

        self.clock = clock.get_default()
        self.event_loop._interval = interval
        
        if interval is None:
            pass # User must call Window.draw() themselves.
        if interval == 0:
            self.clock.schedule(self.event_loop._redraw_windows)
        else:
            self.clock.schedule_interval(self.event_loop._redraw_windows, interval)

        self.event_loop.has_exit = False

        from pyglet.window import Window
        Window._enable_event_queue = False

        # Dispatch pending events
        for window in app.windows:
            window.switch_to()
            window.dispatch_pending_events()
            
        self.event_loop.dispatch_event('on_enter')
        platform_event_loop = app.platform_event_loop
        platform_event_loop.start()
        
        self.event_loop.is_running = True

        while not self.event_loop.has_exit:
            timeout = self.event_loop.idle()
            for child in self.children.values():
                child['window'].run() # Run all children of the Window
            platform_event_loop.step(timeout)

        self.event_loop.is_running = False
        self.event_loop.dispatch_event('on_exit')
        platform_event_loop.stop()

    def create_window(self, *args, **kwargs) -> ComponentWindow:
        window = ComponentWindow( *args, **kwargs)
        self.add(window)
        return window

    def destroy_window(self, name:str) -> None: ...