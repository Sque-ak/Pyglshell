from __future__ import annotations
from typing import List
from abc import ABC, abstractmethod
from pyglshell_types.t_vectors import VEC2, SVEC2

class Layout(ABC): 

    def __init__(self, position:VEC2 = VEC2(0,0), size:SVEC2 = SVEC2(0,0)):
        self._children: List[ABC] = []
        self._min_size:SVEC2 = SVEC2(0,0)
        self._max_size:SVEC2 = SVEC2(0,0)
        self._size:SVEC2 = size
        self._position:VEC2 = position 

    @property
    def children(self) -> List[ABC]:
        return self._children
    
    @children.setter
    def children(self, children:List[ABC]) -> None:
        self._children = children

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
        return self.min_size
    
    @min_size.setter
    def min_size(self, min_size:SVEC2) -> None:
        self._min_size = min_size

    def add(self, element:ABC) -> None:
        self._children.append(element)

    @abstractmethod
    def get_min_size(self) -> SVEC2: ...

    @abstractmethod
    def get_max_size(self) -> SVEC2: ...

    @abstractmethod
    def do_layout(self) -> None: ...


    # class HorizontalStack(Layout):
        
    #     def get_min_size(self) -> SVEC2:
    #         self._min_size=(0,0)

    #         for child in self.children:
    #             if isinstance(child, Window):
    #                 child_size = child.layout.getMinSize()
    #                 self._min_size.width += child_size.width

    #                 if (self._min_size.height < child_size.height):
    #                     self._min_size.height = child_size.height

    #                 return self._min_size
                
    #     def get_desired_size(self) -> SVEC2:
    #         self._desired_size=(0,0)

    #         for child in self.children:
    #             if isinstance(child, Window):
    #                 child_size = child.layout.get_desired_size()
    #                 self._desired_size.width += child_size.width

    #                 if (self._desired_size.height < child_size.height):
    #                     self._desired_size.height = child_size.height

    #                 return self._desired_size            

    #     def get_max_size(self) -> SVEC2:
    #         self._max_size=(0,0)

    #         for child in self.children:
    #             if isinstance(child, Window):
    #                 child_size = child.layout.get_max_size()
    #                 self._max_size.width += child_size.width

    #                 if (self._max_size.height < child_size.height):
    #                     self._max_size.height = child_size.height

    #                 return self._max_size
            

    #     def do_layout(self, window:Window) -> None:
    #         self.get_min_size() # self._min_size
    #         self.get_desired_size() # self._desired_size
    #         self.get_max_size() # self._max_size

    #         if(self._min_size.width >= window.size.width):
    #             for child in self.children:
                    