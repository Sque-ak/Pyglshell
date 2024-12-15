from classes.windows.c_window import Window, WindowsManager
import pyglet

class ComponentWindow(Window): 
        
    def on_init(self) -> None: ...

    def run(self) -> None: ...


class ComponentWindowsManager(WindowsManager):    

    def __init__(self, *args, **kwargs):
        super().__init__()
        self._window = pyglet.window.Window(*args, **kwargs)

    def on_draw(self):
        self._window.clear()

    def on_init(self) -> None:
        self.on_draw = self._window.event(self.on_draw)

        for child in self.children:
            child.on_init()

    def run(self) -> None:
        pyglet.app.run()

        for child in self.children:
            child.run()

    def create_window(self, name:str = 'Window') -> Window:
        window = ComponentWindow(name)
        window.add(self)
        window.on_init()

    def destroy_window(self, name:str) -> None: ...