import pyglet, os
from utils.types.t_vectors import SVEC2

class ICON:
    
    def __init__(self, icon:pyglet.image.AbstractImage | str = pyglet.resource.image('static/favicon.ico'), size:SVEC2 = SVEC2(24,24)):
        self._size = size

        if isinstance(icon, str):
            if os.path.isfile(icon):
                self._icon = pyglet.resource.image(icon)
                self._icon.width = self.size.width
                self._icon.height = self.size.height
        else:
            self._icon = icon

    @property
    def size(self) -> SVEC2:
        return self._size
    
    @size.setter
    def size(self, size:SVEC2) -> None:
        self._size = size

    @property
    def icon(self) -> pyglet.image.AbstractImage:
        return self._icon

    @icon.setter
    def icon(self, path:str) -> None:
        if os.path.isfile(path):
            self._icon = pyglet.resource.image(path)
            self._icon.width = self.size.width
            self._icon.height = self.size.height