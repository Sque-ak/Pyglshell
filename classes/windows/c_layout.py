from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from utils.types.t_vectors import VEC2, SVEC2

class Layout(ABC): 

    def __init__(self, position:VEC2 = VEC2(0,0), size:SVEC2 = SVEC2(0,0)):
        self._children: List[ABC] = []
        self._min_size:SVEC2 = SVEC2(0,0)
        self._max_size:SVEC2 = SVEC2(0,0)
        self._size:SVEC2 = size
        self._position:VEC2 = position 
        self._parent:Layout = None

    @property
    def children(self) -> List[ABC]:
        return self._children
    
    @children.setter
    def children(self, children:List[ABC]) -> None:
        self._children = children

    @property
    def parent(self) -> Layout:
        return self._parent
    
    @parent.setter
    def parent(self, parent:Layout) -> None:
        self._parent = parent

    @property
    def position(self) -> VEC2:
        return self._position
    
    @position.setter
    def position(self, position:VEC2) -> None:
        self._position = position

    @property
    def size(self) -> SVEC2:
        return self._size
    
    @size.setter
    def size(self, size:SVEC2) -> None:
        self._size = size

    @property
    def min_size(self) -> SVEC2:
        return self._min_size
    
    @min_size.setter
    def min_size(self, min_size:SVEC2) -> None:
        self._min_size = min_size

    @property
    def max_size(self) -> SVEC2:
        return self._max_size
    
    @max_size.setter
    def max_size(self, max_size:SVEC2) -> None:
        self._max_size = max_size

    def add(self, element:ABC) -> None:
        if element not in self._children:
            self._children.append(element)

    @abstractmethod
    def get_min_size(self) -> SVEC2: ...

    @abstractmethod
    def get_max_size(self) -> SVEC2: ...

    @abstractmethod
    def do_layout(self) -> None: ...