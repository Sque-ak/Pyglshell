from __future__ import annotations
from typing import Dict
from abc import ABC, abstractmethod

class Window(ABC): 
    """
    Abstract base class representing a window.
    Defines the basic properties and methods that must be implemented in subclasses.
    """
    def __init__(self, name:str = 'Window'):
        self._name: str = name
        self._parent: Window = self
        self._children: Dict[Window] = {}

    @property
    def children(self) -> Dict[Window]:
        return self._children
    
    @children.setter
    def children(self, children: Dict[Window]) -> None:
        self._children = children

    @property
    def parent(self) -> Window:
        """ The parent of the window."""
        return self._parent
    
    @parent.setter
    def parent(self, parent: Window) -> None:
        """ Are you can sets the new parent of the window. """
        self._parent = parent

    @property
    def name(self) -> str:
        """ The name of the window. """
        return self._name
    
    @name.setter
    def name(self, name: str):
        """ Sets the name of the window. """
        self._name = name

    def get_manager(self) -> WindowsManager:
        """Returns the window manager to which the current window belongs."""
        if self.is_windows_manager() or self.parent == self:
            return self
        else:
            return self.parent.get_manager()

    def is_exist(self, window: Window) -> bool:
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
    
    def set_nonexistant_name(self, window: Window, index = 1) -> Window:
        """ Sets a unique name for the window if the current name already exists.

            :param window: The window for which the name is being set.
            :param index: Index for name uniqueness.
            :return: The window with a unique name.
         """
        if window.name in self._children:
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
    
    def add(self, window: Window) -> None:
        """
        Adds a window to the collection, ensuring it has a unique name.
        Sets the parent of the added window to the current window.
        """
        self.set_nonexistant_name(window)
        self._children = self._children | {window.name : { 'window': window, 'name': window.name}}
        window.parent = self
    
    def remove(self, window: Window) -> None:   
        """
        Removes a specified window from the collection.
        If the window is found, it is deleted from the collection.
        """     
        if self._children[window.name]:
            del self._children[window.name]
            window.parent = window

    def get(self, name:str) -> Window:
        """
        Retrieves a window by its name from the collection.
        If not found, the method attempts to retrieve it from child windows recursively.
        """
        if len(self._children) == 0:
            return None
        
        if self._children[name]:
            return self._children[name]['window']
        else:
            for _child in self._children:
                return _child.get(_child, name)

    @abstractmethod        
    def on_init(self) -> None: ...

    @abstractmethod
    def run(self) -> None: ...


class WindowsManager(Window):    

    def __init__(self):
        super().__init__()
        self._name = 'WindowsManager'
        self._window: any = None

    @property
    def window(self):
        return self._window
    
    @window.setter
    def window(self, window):
        self._window = window

    def is_windows_manager(self) -> bool:
        return True
    
    def is_composite(self) -> bool:
        return True

    @abstractmethod
    def create_window(self, name:str) -> Window: ...

    @abstractmethod
    def destroy_window(self, name:str) -> None: ...