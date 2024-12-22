class VEC2:
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
    
class VEC3:
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
    
class SVEC2(VEC2):
    
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