from typing import List
from abc import ABC, abstractmethod
from pydantic import BaseModel
from utils.types.t_vectors import VEC2, SVEC2

class Layout(ABC, BaseModel): 
    '''
    The `Layout` class is an abstract base class that represents a layout for a user interface element. 
    It provides a set of properties and methods for managing the size, position, and children of the layout. 
    The class is designed to be subclassed by concrete layout implementations, which must provide implementations for the abstract methods `get_min_size()`, `get_max_size()`, and `do_layout()`.
    '''

    children: List[BaseModel] = []
    parent: 'Layout' = None
    position:VEC2 = VEC2(0,0)
    size:SVEC2 = SVEC2(0,0)
    max_size:SVEC2 = SVEC2(0,0)
    min_size:SVEC2 = SVEC2(0,0)

    def add(self, element:BaseModel) -> None:
        '''
        Adds the given element to the list of children for this layout, if it is not already present.
        
        Parameters:
            element (BaseModel): The element to add as a child of this layout.
        '''
        if element not in self.children:
            self.children.append(element)

    @abstractmethod
    def get_min_size(self) -> SVEC2: ...

    @abstractmethod
    def get_max_size(self) -> SVEC2: ...

    @abstractmethod
    def do_layout(self) -> None: ...