"""
This module defines several vector and grid classes for 2D and 3D vector operations.

The `VEC2` and `VEC3` classes represent 2D and 3D vectors, respectively, and provide properties and methods for accessing and modifying the vector components, as well as performing basic vector operations such as addition, subtraction, scalar multiplication, and dot product.

The `SVEC2` and `SVEC3` classes are subclasses of `VEC2` and `VEC3`, respectively, and represent 2D and 3D vectors with additional properties for width and height (or depth).

The `GRID4` class represents a 2D grid defined by its west, east, north, and south boundaries, and provides methods for performing grid-related operations such as addition, subtraction, and scalar multiplication.

All of these classes are designed to be used as part of a larger application or library, and are intended to provide a consistent and easy-to-use interface for working with 2D and 3D vector and grid data.
"""
from pydantic_core import core_schema

class VEC2:
    '''
    A 2D vector class with properties for accessing and modifying the x and y components. 
    Supports basic vector operations such as addition, subtraction, and scalar multiplication.

    Args:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
    '''
    def __init__(self, x: float, y: float):
        self._x = x
        self._y = y

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, x:float) -> None:
        self._x = x

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, y:float) -> None:
        self._y = y

    def __repr__(self):
        return f"VEC2(x={self._x}, y={self._y})"

    def __eq__(self, other):
        if isinstance(other, VEC2):
            return self._x == other.x and self._y == other.y
        return False

    def __add__(self, other):
        if isinstance(other, VEC2):
            return VEC2(self._x + other.x, self._y + other.y)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, VEC2):
            return VEC2(self._x - other.x, self._y - other.y)
        return NotImplemented

    def __mul__(self, scalar: float):
        return VEC2(self._x * scalar, self._y * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def dot(self, other):
        if isinstance(other, VEC2):
            return self._x * other.x + self._y * other.y 
        return NotImplemented
    
    def __get_pydantic_core_schema__(self, handler):
        return core_schema.typed_dict_schema({
                'x': core_schema.typed_dict_field(core_schema.float_schema()),
                'y': core_schema.typed_dict_field(core_schema.float_schema()),
            })

class VEC3:
    '''
    Represents a 3D vector with x, y, and z components.
    Args:
        x (float): The x-coordinate of the vector.
        y (float): The y-coordinate of the vector.
        z (float): The z-coordinate of the vector.
    '''
    def __init__(self, x: float, y: float, z: float):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self) -> float:
        return self._x
    
    @x.setter
    def x(self, x:float) -> None:
        self._x = x

    @property
    def y(self) -> float:
        return self._y
    
    @y.setter
    def y(self, y:float) -> None:
        self._y = y

    @property
    def z(self) -> float:
        return self._z
    
    @z.setter
    def z(self, z:float) -> None:
        self._z = z

    def __repr__(self):
        return f"VEC3(x={self._x}, y={self._y}, z={self._z})"

    def __eq__(self, other):
        if isinstance(other, VEC3):
            return self._x == other.x and self._y == other.y and self._z == other.z
        return False

    def __add__(self, other):
        if isinstance(other, VEC3):
            return VEC3(self._x + other.x, self._y + other.y, self._z + other.z)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, VEC3):
            return VEC3(self._x - other.x, self._y - other.y, self._z - other.z)
        return NotImplemented

    def __mul__(self, scalar: float):
        return VEC3(self._x * scalar, self._y * scalar, self._z * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def dot(self, other):
        if isinstance(other, VEC3):
            return self._x * other.x + self._y * other.y + self._z * other.z
        return NotImplemented

    def cross(self, other):
        if isinstance(other, VEC3):
            return VEC3(
                self._y * other.z - self._z * other.y,
                self._z * other.x - self._x * other.z,
                self._x * other.y - self._y * other.x
            )
        return NotImplemented
    
    def __get_pydantic_core_schema__(self, handler):
        return core_schema.typed_dict_schema({
                'x': core_schema.typed_dict_field(core_schema.float_schema()),
                'y': core_schema.typed_dict_field(core_schema.float_schema()),
                'z': core_schema.typed_dict_field(core_schema.float_schema()),
            })
    
class SVEC2(VEC2):
    """
    A 2D vector class with additional properties for width and height.
    
    The `SVEC2` class inherits from the `VEC2` class and adds properties for accessing and setting the width and height of the vector. 
    This can be useful for working with 2D shapes or other 2D data structures that have a defined width and height.

    Args:
        width (float): The width of the vector.
        height (float): The height of the vector.
    """
        
    def __init__(self, width: float, height: float):
        self._x = self._width = width
        self._y = self._height = height

    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, width:float) -> None:
        self._width = width

    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, height:float) -> None:
        self._height = height



class SVEC3(VEC3):
    """
    A 3D vector class with additional properties for width, height, and depth.
    
    The `SVEC3` class inherits from the `VEC3` class and adds properties for accessing and setting the width, height, and depth of the vector.
    This can be useful for working with 3D shapes or other 3D data structures that have a defined width, height, and depth.

    Args:
        width (float): The width of the vector.
        height (float): The height of the vector.
        depth (float): The depth of the vector.
    """
        
    def __init__(self, width: float, height: float, depth: float):
        self._x = self._width = width
        self._y = self._height = height
        self._z = self._depth = depth

    @property
    def width(self) -> float:
        return self._width
    
    @width.setter
    def width(self, width:float) -> None:
        self._width = width

    @property
    def height(self) -> float:
        return self._height
    
    @height.setter
    def height(self, height:float) -> None:
        self._height = height

    @property
    def depth(self) -> float:
        return self._depth
    
    @depth.setter
    def depth(self, depth:float) -> None:
        self._depth = depth

class GRID4:
    '''
    A 2D grid representation with properties for the west, east, north, and south bounds.
    
    The `GRID4` class provides a convenient way to work with 2D grids or bounding boxes. 
    It has properties for accessing and setting the west, east, north, and south bounds of the grid, as well as methods for performing common operations like addition, subtraction, and dot product.
    This class can be useful for tasks like spatial analysis, geographic information systems, or any other applications that require working with 2D grids or bounding boxes.

    Args:
        west (float): The west bound of the grid.
        east (float): The east bound of the grid.
        north (float): The north bound of the grid.
        south (float): The south bound of the grid.
    '''

    def __init__(self, west: float, east: float, north: float, south: float):
        self._west = west
        self._east = east
        self._north = north
        self._south = south

    @property
    def west(self) -> float:
        return self._west
    
    @west.setter
    def west(self, west:float) -> None:
        self._west = west

    @property
    def east(self) -> float:
        return self._east
    
    @east.setter
    def east(self, east:float) -> None:
        self._east = east

    @property
    def north(self) -> float:
        return self._north
    
    @north.setter
    def north(self, north:float) -> None:
        self._north = north

    @property
    def south(self) -> float:
        return self._south
    
    @south.setter
    def south(self, south:float) -> None:
        self._south = south

    def __repr__(self):
        return f"GRID(west={self.west}, east={self.east}, north={self.north}, south={self.south})"

    def __eq__(self, other):
        if isinstance(other, GRID4):
            return self.west == other.west and self.east == other.east and self.north == other.north and self.south == other.south
        return False

    def __add__(self, other):
        if isinstance(other, GRID4):
            return GRID4(self.west + other.west, self.east + other.east, self.north + other.north, self.south + other.south)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, GRID4):
            return GRID4(self.west - other.west, self.east - other.east, self.north - other.north, self.south - other.south)
        return NotImplemented

    def __mul__(self, scalar: float):
        return GRID4(self.west * scalar, self.east * scalar, self.north * scalar, self.south * scalar)

    def __rmul__(self, scalar: float):
        return self.__mul__(scalar)

    def dot(self, other):
        if isinstance(other, GRID4):
            return self.west * other.west + self.east * other.east + self.north * other.north + self.south * other.south
        return NotImplemented
    
    def __get_pydantic_core_schema__(self, handler):
        return core_schema.typed_dict_schema({
                'west': core_schema.typed_dict_field(core_schema.float_schema()),
                'east': core_schema.typed_dict_field(core_schema.float_schema()),
                'north': core_schema.typed_dict_field(core_schema.float_schema()),
                'south': core_schema.typed_dict_field(core_schema.float_schema()),
            })