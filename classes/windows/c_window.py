from pydantic import BaseModel, Field
from pyglet.clock import Clock
from utils.types.t_vectors import SVEC2, VEC2
from classes.windows.c_layout import Layout
from utils.components.layout import ComponentHorizontalStack
import random
from abc import ABC, abstractmethod

class Window(ABC, BaseModel):
    """
    The `Window` class is an abstract base class that represents a window in a graphical user interface. It provides a set of properties and methods for managing the window's appearance, behavior, and layout.

    The class has the following key features:

    - Support for parent-child relationships between windows, allowing for the creation of complex window hierarchies.
    - Configurable size, position, anchor, and layout properties.
    - Methods for checking the existence of a window, determining if it is a window manager or composite, and setting a unique name for a window.
    - Methods for adding and removing windows from the window collection, as well as retrieving windows by name.
    - Abstract methods for drawing, initializing, and running the window, which must be implemented by concrete subclasses.

    The `Window` class is designed to be extended by specific window implementations, which can override the abstract methods and customize the window's behavior as needed.
    """
    def generate_name(self)-> str:
        NAMES = [
            "WackyWindow",
            "JollyWindow",
            "BouncyWindow",
            "CheeryWindow",
            "SnazzyWindow",
            "ZippyWindow",
            "QuirkyWindow",
            "PeppyWindow",
            "GigglyWindow",
            "WhimsicalWindow",
            "FunkyWindow",
            "BreezyWindow",
            "ChirpyWindow",
            "PerkyWindow",
            "SpunkyWindow"
        ]
        return random.choice(NAMES)

    name:str = Field(default_factory=generate_name)
    parent: 'Window' = None
    children: 'Window' = {}
    size: SVEC2 = SVEC2(200,200)
    position:VEC2 = VEC2(0,0)
    anchor:str = 'north'
    fixed:bool = True
    layout:'Layout' = ComponentHorizontalStack()
    min_size:SVEC2 = SVEC2(50,50)
    max_size:SVEC2 = SVEC2(0,0)
    bevel:VEC2 = VEC2(15,15)

    def __init__(self, **data):
        super().__init__(**data)
        if self.parent is None:
            self.parent = self

    def get_min_size(self) -> SVEC2:
        return self.min_size
    
    def get_max_size(self) -> SVEC2:
        return self.max_size 

    def get_manager(self) -> 'WindowsManager':
        """Returns the window manager to which the current window belongs."""
        if self.is_windows_manager() or self.parent == self:
            return self
        else:
            return self.parent.get_manager()

    def is_exist(self, window: 'Window') -> bool:
        """ Checks if the window exists in the current window. """
        if self.is_composite():
            return window.name in self._children
        else:
            return self

    def is_windows_manager(self) -> bool:
        """ Checks if the current window is a window manager. """
        return False
    
    def is_composite(self) -> bool:
        """ Checks if the current window is composite. """
        return False
    
    def set_nonexistant_name(self, window: 'Window', index = 1) -> 'Window':
        """ Sets a unique name for the window if the current name already exists.

            :param window: The window for which the name is being set.
            :param index: Index for name uniqueness.
            :return: The window with a unique name.
         """
        if window.name in self.children:
            _name = window.name.split('_')

            if _name[-1].isdigit():
                index = int(_name[-1])+1
                _name = ''.join(_name[:-1]) + f'_{index}'
            else:
                _name = window.name + f'_{index}'

            window.name = _name
            self.set_nonexistant_name(window, index)
        else:
            return window
    
    def add(self, window: 'Window') -> None:
        """
        Adds a window to the collection, ensuring it has a unique name.
        Sets the parent of the added window to the current window.
        """
        self.set_nonexistant_name(window)
        self.children = self.children | {window.name : { 'window': window, 'name': window.name}}
        self.layout.add(window)
        window.parent = self
    
    def remove(self, window: 'Window') -> None:   
        """
        Removes a specified window from the collection.
        If the window is found, it is deleted from the collection.
        """     
        if self.children[window.name]:
            del self.children[window.name]
            window.parent = window

    def get(self, name:str) -> 'Window':
        """
        Retrieves a window by its name from the collection.
        If not found, the method attempts to retrieve it from child windows recursively.
        """
        if len(self.children) == 0:
            return None
        
        if self.children[name]:
            return self.children[name]['window']
        else:
            for _child in self.children:
                return _child.get(_child, name)

    @abstractmethod
    def on_draw(self) -> None: ...

    def on_redraw(self) -> None: ...

    def on_resize(self, width:int = 0, height:int = 0) -> None: ...

    @abstractmethod        
    def on_init(self) -> None: ...

    @abstractmethod
    def run(self) -> None: ...


class WindowsManager(Window): 
    '''
    The `WindowsManager` class is responsible for managing a collection of windows. 
    It provides methods to add, remove, and retrieve windows by name, as well as handle events such as drawing, redrawing, and resizing. 
    The class also includes utility methods like `generate_name()` to generate unique window names, and properties to store a `BaseModel` and a `Clock` instance.
    '''
    def generate_name(self):
        NAMES = [
            "WindowsManager",
            "FunnyWindowsManager",
            "WackyWindowsManager",
            "JollyWindowsManager",
            "BouncyWindowsManager",
            "CheeryWindowsManager",
            "SnazzyWindowsManager",
            "ZippyWindowsManager",
            "QuirkyWindowsManager",
            "PeppyWindowsManager",
            "GigglyWindowsManager",
            "WhimsicalWindowsManager",
        ]
        return random.choice(NAMES)

    window: BaseModel = None
    clock: Clock = None

    class Config:
        arbitrary_types_allowed = True

    def is_windows_manager(self) -> bool:
        # This is element is window manager
        return True
    
    def is_composite(self) -> bool:
        return True
    

    @abstractmethod
    def create_window(self, name:str) -> Window: ...

    @abstractmethod
    def destroy_window(self, name:str) -> None: ...