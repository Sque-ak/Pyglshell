from classes.windows.c_layout import Layout
from utils.types.t_vectors import VEC2, SVEC2

class ComponentHorizontalStack(Layout):

    def __init__(self, bevel:VEC2 = VEC2(15,15), margin:VEC2 = VEC2(25,25), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel:VEC2 = bevel
        self._margin:VEC2 = margin
        
    def get_min_size(self) -> SVEC2:
        self._min_size = self.position + SVEC2(self._bevel.x, self._bevel.y)
        return SVEC2(self._min_size.x, self._min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size - SVEC2(self._bevel.x*2, self._bevel.y*2)
        return SVEC2(self._max_size.x, self._max_size.y)

    def do_layout(self):

        if len(self.children) > 0:

            if not (self.parent):
                manager = self.children[0].get_manager()
                self.position = VEC2(0,0)
                self.size = manager.size

            self._min_size = self.get_min_size()
            self._max_size = self.get_max_size()

            len_children = len(self.children)

            for index, child in enumerate(self.children):

                child.size = SVEC2((self._max_size.width - (self._margin.x * (len_children - 1)))/len_children, self._max_size.height)
                child.position = VEC2((self._min_size.x + (index*(child.size.width + self._margin.y))), self._min_size.y)



class ComponentVerticalStack(Layout):

    def __init__(self, bevel:VEC2 = VEC2(15,15), margin:VEC2 = VEC2(25,25), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel:VEC2 = bevel
        self._margin:VEC2 = margin
        
    def get_min_size(self) -> SVEC2:
        self._min_size = self.position + SVEC2(self._bevel.x, self._bevel.y)
        return SVEC2(self._min_size.x, self._min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size - SVEC2(self._bevel.x*2, self._bevel.y*2)
        return SVEC2(self._max_size.x, self._max_size.y)

    def do_layout(self) -> None:

        if len(self.children) > 0:

            if not (self.parent):
                manager = self.children[0].get_manager()
                self.position = VEC2(0,0)
                self.size = manager.size

            self._min_size = self.get_min_size()
            self._max_size = self.get_max_size()

            len_children = len(self.children)

            for index, child in enumerate(self.children):

                child.size = SVEC2(self._max_size.width, (self._max_size.height - (self._margin.x * (len_children - 1)))/len_children)
                child.position = VEC2(self._min_size.x, self._min_size.y  + (index*(child.size.height + self._margin.y)))

class ComponentBorderStack(Layout):

    def __init__(self, north_height:int = 64, south_height:int = 64, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._north = ComponentVerticalStack(bevel=VEC2(5,5), margin=VEC2(5,5))
        self._center = ComponentHorizontalStack(bevel=VEC2(5,0), margin=VEC2(5,5))
        self._south = ComponentVerticalStack(bevel=VEC2(5,5), margin=VEC2(5,5))
        self._north.parent = self
        self._center.parent = self
        self._south.parent = self
        self._north_height = north_height
        self._south_height = south_height

    @property
    def north(self) -> ComponentVerticalStack:
        return self._north
    
    @property
    def center(self) -> ComponentHorizontalStack:
        return self._center
    
    @property
    def south(self) -> ComponentVerticalStack:
        return self._south
        
    def get_min_size(self) -> SVEC2:
        self._min_size = self.position
        return SVEC2(self._min_size.x, self._min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size
        return SVEC2(self._max_size.x, self._max_size.y)

    def on_init(self) -> None: 
        if len(self.children) > 0:
            __west = []
            __center = []
            __east = []

            for child in self._children:
                match child.anchor:
                    case 'north':
                        self.north.add(child)
                    case 'center':
                        __center.append(child)
                    case 'west':
                        __west.append(child)
                    case 'east':
                        __east.append(child)
                    case 'south':
                        self.south.add(child)

            for west in __west:
                self.center.add(west)
            
            for center in __center:
                self.center.add(center)

            for east in __east:
                self.center.add(east)

    def do_layout(self) -> None:

        if not (self.parent):
            manager = self.children[0].get_manager()
            self.position = VEC2(0,0)
            self.size = manager.size

        self.north.position = VEC2(self.position.x, self.position.y)
        self.north.size = SVEC2(self.size.x, self._north_height)

        self.south.position = VEC2(self.position.x, self.size.y - self._south_height)
        self.south.size = SVEC2(self.size.x, self._south_height)

        self.center.position = VEC2(self.position.x, self.position.y + self._north_height)
        self.center.size = SVEC2(self.size.x, self.size.y - self._north_height - self._south_height)

        self.north.do_layout()
        self.center.do_layout()
        self.south.do_layout()

            
                        

                
        