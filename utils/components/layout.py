from classes.windows.c_layout import Layout
from utils.types.t_vectors import VEC2, SVEC2, GRID4

class ComponentHorizontalStack(Layout):
    '''
        The `ComponentHorizontalStack` class is a layout component that arranges child components in a horizontal stack. It uses the `Layout` base class to provide the core layout functionality.
        
        The class has the following key features:
        
        - Supports setting the bevel and margin sizes for the layout.
        - Provides methods to calculate the minimum and maximum size of the layout.
        - The `do_layout()` method is responsible for positioning and sizing the child components based on the available space and the constraints of the layout.
        - It determines the flexible and fixed-size children, and calculates the flexible width to distribute the remaining space accordingly.
        - The child components are positioned and sized starting from the left of the layout, considering the bevel and margin.

        Args:
            bevel (VEC2, optional): The bevel size for the layout. Defaults to VEC2(15, 15).
            margin (VEC2, optional): The margin size for the layout. Defaults to VEC2(25, 25).
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
    '''
    def __init__(self, bevel:VEC2 = VEC2(15,15), margin:VEC2 = VEC2(25,25), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel:VEC2 = bevel
        self._margin:VEC2 = margin
        
    def on_init(self) -> None: ...

    def get_min_size(self) -> SVEC2:
        return self.min_size

    def get_max_size(self) -> SVEC2:
        self.max_size = self.size - SVEC2(self._bevel.x*2, self._bevel.y*2)
        return SVEC2(self.max_size.x, self.max_size.y)

    def do_layout(self) -> None:
        if len(self.children) > 0:
            if not self.parent:
                manager = self.children[0].get_manager()
                self.position = VEC2(0, 0)
                self.size = manager.size

            self.max_size = self.get_max_size()
            __len_children = len(self.children)

            # Calculate total space occupied by fixed-size windows
            __fixed_width_total = sum(child.min_size.x for child in self.children)

            # Calculate remaining width for flexible children
            __remaining_width = max(self.size.x - __fixed_width_total - self._margin.x * (__len_children - 1), 0) - self._bevel.x * 2

            # Determine the flexible children based on current size constraints
            __flexible_children = [child for child in self.children if (((child.size.x >= child.min_size.x) or child.min_size.x == 0) and child.max_size.x == 0)]

            # Calculate flexible width only for flexible children
            if __flexible_children:
                __flexible_width = (__remaining_width / len(__flexible_children))
            else:
                __flexible_width = __remaining_width / 1

            # Set sizes and positions for each child
            __current_x = self.position.x + self._bevel.x # Start from the left, considering left bevel

            for child in self.children:
                # Calculate the width for each child considering min and max constraints
                if child in __flexible_children:
                    __child_width = max(child.min_size.x, child.min_size.x + __flexible_width)
                else:
                    __child_width = child.min_size.x
                    if child.max_size.x > 0:
                        __child_width = min(__child_width, child.max_size.x)

                # Update the current position accounting for the margin
                child.size = SVEC2(__child_width, self.max_size.y)
                child.position = VEC2(__current_x, self.position.y + self._bevel.y)

                # Move right by the width of the current element and add margin
                __current_x += __child_width
                __current_x += self._margin.x


class ComponentVerticalStack(Layout):
    '''
        The `ComponentVerticalStack` class is a layout component that arranges child components in a vertical stack. It uses the `Layout` base class to provide the core layout functionality.
        
        The class has the following key features:
        
        - Supports setting the bevel and margin sizes for the layout.
        - Provides methods to calculate the minimum and maximum size of the layout.
        - The `do_layout()` method is responsible for positioning and sizing the child components based on the available space and the constraints of the layout.
        - It determines the flexible and fixed-size children, and calculates the flexible height to distribute the remaining space accordingly.
        - The child components are positioned and sized starting from the bottom of the layout, considering the bevel and margin.

        Args:
            bevel (VEC2, optional): The bevel size for the layout. Defaults to VEC2(15, 15).
            margin (VEC2, optional): The margin size for the layout. Defaults to VEC2(25, 25).
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
    '''   
    def __init__(self, bevel:VEC2 = VEC2(15,15), margin:VEC2 = VEC2(25,25), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._bevel:VEC2 = bevel
        self._margin:VEC2 = margin
        
    def on_init(self) -> None: ...

    def get_min_size(self) -> SVEC2:
        return self.min_size

    def get_max_size(self) -> SVEC2:
        self.max_size = self.size - SVEC2(self._bevel.x*2, self._bevel.y*2)
        return SVEC2(self.max_size.x, self.max_size.y)

    def do_layout(self) -> None:
        if len(self.children) > 0:
            if not self.parent:
                manager = self.children[0].get_manager()
                self.position = VEC2(0, 0)
                self.size = manager.size

            self.max_size = self.get_max_size()
            __len_children = len(self.children)

            # Calculate total space occupied by fixed-size windows
            __fixed_height_total = sum(child.min_size.y for child in self.children)

            # Calculate remaining height for flexible children
            __remaining_height = max(self.size.y - __fixed_height_total - self._margin.y * (__len_children - 1), 0) - self._bevel.y *2

            # Determine the flexible children based on current size constraints
            __flexible_children = [child for child in self.children if (((child.size.y >= child.min_size.y) or child.min_size.y == 0) and child.max_size.y == 0)]

            # Calculate flexible height only for flexible children
            if __flexible_children:
                __flexible_height = (__remaining_height / len(__flexible_children))
            else:
                __flexible_height = __remaining_height / 1

            # Set sizes and positions for each child
            __current_y = self.size.y - self._bevel.y  # Start from the bottom, considering bottom bevel

            for child in self.children:
                # Calculate the height for each child considering min and max constraints
                if child in __flexible_children:
                    __child_height = max(child.min_size.y, child.min_size.y + __flexible_height)
                else:
                    __child_height = child.min_size.y
                    if child.max_size.y > 0:
                        __child_height = min(__child_height, child.max_size.y)

                # Update the current position accounting for the margin
                __current_y -= __child_height
                child.size = SVEC2(self.max_size.x, __child_height)
                child.position = VEC2(self.position.x + self._bevel.x, __current_y + self.position.y)
                    
                __current_y -= self._margin.y


class ComponentBorderStack(Layout):
    '''
        The `ComponentBorderStack` class is a layout component that arranges child components in a border layout, with a north, south, west, east, and center region.
        It uses `ComponentVerticalStack` instances to manage the layout of the child components in each region. 
        The class provides properties to access the individual regions, as well as methods to calculate the minimum and maximum size of the layout. 
        The `do_layout()` method is responsible for positioning and sizing the child components based on the available space and the constraints of the layout.

        Args:
            bevel (VEC2, optional): The bevel size for the layout. Defaults to VEC2(5,5).
            margin (VEC2, optional): The margin size for the layout. Defaults to VEC2(5,5).
            grid (GRID4, optional): The grid size for the layout. Defaults to GRID4(480,480,50,50).
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.
    '''

    def __init__(self, bevel:VEC2 = VEC2(5,5), margin:VEC2 = VEC2(5,5), grid:GRID4 = GRID4(480,480,50,50), *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._north = ComponentVerticalStack(bevel=VEC2(bevel.x,bevel.y), margin=VEC2(margin.x,margin.y))
        self._center = ComponentVerticalStack(bevel=VEC2(0,0), margin=VEC2(margin.x,margin.y))
        self._south = ComponentVerticalStack(bevel=VEC2(bevel.x,bevel.y), margin=VEC2(margin.x,margin.y))
        self._west = ComponentVerticalStack(bevel=VEC2(bevel.x,0), margin=VEC2(margin.x,margin.y))
        self._east = ComponentVerticalStack(bevel=VEC2(bevel.x,0), margin=VEC2(margin.x,margin.y))
        self._north.parent = self
        self._center.parent = self
        self._south.parent = self
        self._west.parent = self.center
        self._east.parent = self.center
        self._grid = grid
        self._bevel = bevel
        self._margin = margin

    @property
    def grid(self) -> GRID4:
        return self._grid
    
    @grid.setter
    def grid(self, grid:GRID4):
        self._grid = grid
                
    @property
    def north(self) -> ComponentVerticalStack:
        return self._north
    
    @property
    def center(self) -> ComponentHorizontalStack:
        return self._center
    
    @property
    def south(self) -> ComponentVerticalStack:
        return self._south
    
    @property
    def west(self) -> ComponentVerticalStack:
        return self._west
    
    @property
    def east(self) -> ComponentVerticalStack:
        return self._east
        
    def get_min_size(self) -> SVEC2:
        self.min_size = self.position
        return SVEC2(self.min_size.x, self.min_size.y)

    def get_max_size(self) -> SVEC2:
        self._max_size = self.size
        return SVEC2(self.max_size.x, self.max_size.y)

    def on_init(self) -> None: 

        for child in self.children:
            match child.anchor:
                case 'north':
                    self.north.add(child)
                case 'center':
                    self.center.add(child)
                case 'west':
                    self.west.add(child)
                case 'east':
                    self.east.add(child)
                case 'south':
                    self.south.add(child)


    def do_layout(self) -> None:
        if not self.parent:
            manager = self.children[0].get_manager()
            self.position = VEC2(0, 0)
            self.size = manager.size

        # Calculate grid sizes for each region
        __grid_size = GRID4(
            max(self.west.get_min_size().x, self.grid.west) if len(self.west.children) > 0 else self._bevel.x,
            max(self.east.get_min_size().x, self.grid.east) if len(self.east.children) > 0 else self._bevel.x,
            max(self.north.get_min_size().y, self.grid.north) if len(self.north.children) > 0 else self._bevel.y,
            max(self.south.get_min_size().y, self.grid.south) if len(self.south.children) > 0 else self._bevel.y
        )

        # Calculate available space for center
        __total_vertical_space = self.size.y - __grid_size.north - __grid_size.south
        __total_horizontal_space = self.size.x - __grid_size.west - __grid_size.east

        # Ensure north and south do not exceed available vertical space
        if __total_vertical_space < 0:
            __grid_size.north = self.size.y / 2
            __grid_size.south = self.size.y / 2
            __total_vertical_space = 0

        # Ensure west and east do not exceed available horizontal space
        if __total_horizontal_space < 0:
            __grid_size.west = self.size.x / 2
            __grid_size.east = self.size.x / 2
            __total_horizontal_space = 0

        # Position and size north
        self.north.position = VEC2(self.position.x, self.position.y + self.size.y - __grid_size.north)
        self.north.size = SVEC2(self.size.x, __grid_size.north)

        # Position and size south
        self.south.position = VEC2(self.position.x, self.position.y)
        self.south.size = SVEC2(self.size.x, __grid_size.south)

        # Position and size west
        self.west.position = VEC2(self.position.x, self.position.y + __grid_size.south)
        self.west.size = SVEC2(__grid_size.west, __total_vertical_space - (self._bevel.y * 2 if len(self.north.children) > 0 else 0))

        # Position and size east
        self.east.position = VEC2(self.position.x + self.size.x - __grid_size.east, self.position.y + __grid_size.south)
        self.east.size = SVEC2(__grid_size.east, __total_vertical_space - (self._bevel.y * 2 if len(self.north.children) > 0 else 0))

        # Ensure center takes all available space
        if len(self.center.children) > 0:
            self.center.position = VEC2(self.position.x + __grid_size.west, self.position.y + __grid_size.south)
            self.center.size = SVEC2(__total_horizontal_space, __total_vertical_space - (self._bevel.y * 2 if len(self.north.children) > 0 else 0))

        # Layout all regions
        self.north.do_layout()
        self.center.do_layout()
        self.south.do_layout()
        self.west.do_layout()
        self.east.do_layout()

