from classes.windows.c_layout import Layout
from utils.types.t_vectors import VEC2, SVEC2

class ComponentHorizontalStack(Layout):

    def __init__(self, bevel:float = 15, margin:float = 25, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel = bevel
        self._margin = margin
        
    def get_min_size(self) -> SVEC2:
        self._min_size = self.position + SVEC2(self._bevel, self._bevel)
        return SVEC2(self._min_size.x, self._min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size - SVEC2(self._bevel*2, self._bevel*2)
        return SVEC2(self._max_size.x, self._max_size.y)

    def do_layout(self) -> None:

        if len(self.children) > 0:
            from classes.windows.c_window import Window

            if isinstance(self.children[0], Window):
                manager = self.children[0].get_manager()
                self.position = VEC2(0,0)
                self.size = manager.size

            self._min_size = self.get_min_size()
            self._max_size = self.get_max_size()

            len_children = len(self.children)

            for index, child in enumerate(self.children):

                if isinstance(child, Window):
                    child.size = SVEC2((self._max_size.width - (self._margin * (len_children - 1)))/len_children, self._max_size.height)
                    child.position = VEC2((self._min_size.x + (index*(child.size.width + self._margin))), self._min_size.y)

class ComponentVerticalStack(Layout):

    def __init__(self, bevel:float = 15, margin:float = 25, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel = bevel
        self._margin = margin
        
    def get_min_size(self) -> SVEC2:
        self._min_size = self.position + SVEC2(self._bevel, self._bevel)
        return SVEC2(self._min_size.x, self._min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size - SVEC2(self._bevel*2, self._bevel*2)
        return SVEC2(self._max_size.x, self._max_size.y)

    def do_layout(self) -> None:

        if len(self.children) > 0:
            from classes.windows.c_window import Window

            if isinstance(self.children[0], Window):
                manager = self.children[0].get_manager()
                self.position = VEC2(0,0)
                self.size = manager.size

            self._min_size = self.get_min_size()
            self._max_size = self.get_max_size()

            len_children = len(self.children)

            for index, child in enumerate(self.children):

                if isinstance(child, Window):
                    child.size = SVEC2(self._max_size.width, (self._max_size.height - (self._margin * (len_children - 1)))/len_children)
                    child.position = VEC2(self._min_size.x, self._min_size.y  + (index*(child.size.height + self._margin)))