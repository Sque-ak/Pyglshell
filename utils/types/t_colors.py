from pydantic_core import core_schema

class RGB:
    '''
    Represents an RGB color value. Provides methods for performing arithmetic operations on RGB values, such as addition and subtraction.
    Args:
        r (int): The red component of the color value.
        g (int): The green component of the color value.
        b (int): The blue component of the color value.
    '''

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return (self.r, self.g, self.b)

    def __eq__(self, other):
        if isinstance(other, RGB):
            return self.r == other.r and self.g == other.g and self.b == other.b
        return False
    
    def __sub__(self, other):
        if isinstance(other, RGB):
            return RGB(
                max(0, self.r - other.r),
                max(0, self.g - other.g),
                max(0, self.b - other.b),
            )
        elif isinstance(other, RGBA):
            return RGBA(
                max(0, self.r - other.r),
                max(0, self.g - other.g),
                max(0, self.b - other.b),
                max(0, other.a)
            )
        elif isinstance(other, int):
            return RGB(
                max(0, self.r - other),
                max(0, self.g - other),
                max(0, self.b - other),
            )
        raise TypeError("Subtraction only supported between RGB and RGB/RGBA/int instances")
    

    def __add__(self, other):
        if isinstance(other, RGB):
            return RGB(
                min(255, self.r + other.r),
                min(255, self.g + other.g),
                min(255, self.b + other.b),
            )
        elif isinstance(other, RGBA):
            return RGBA(
                min(255, self.r + other.r),
                min(255, self.g + other.g),
                min(255, self.b + other.b),
                min(255, other.a)
            )
        elif isinstance(other, int):
            return RGB(
                min(255, self.r + other),
                min(255, self.g + other),
                min(255, self.b + other),
            )
        raise TypeError("Addition only supported between RGB and RGB/RGBA/int instances")
    
    def __get_pydantic_core_schema__(self, handler):
        return core_schema.typed_dict_schema({
                'r': core_schema.typed_dict_field(core_schema.int_schema()),
                'g': core_schema.typed_dict_field(core_schema.int_schema()),
                'b': core_schema.typed_dict_field(core_schema.int_schema()),
            })

class RGBA:
    '''
    Represents an RGBA color with 8-bit integer values for the red, green, blue, and alpha (transparency) channels.
    
    The RGBA class provides methods for performing arithmetic operations on RGBA colors, such as addition and subtraction. 
    These operations are defined to handle different input types (RGB, RGBA, integers) and ensure the resulting values are clamped to the valid range of 0-255.
    The class also includes a method to generate a Pydantic core schema for the RGBA type, which can be used for data validation and serialization.

    Args:
        r (int): The red component of the color value.
        g (int): The green component of the color value.
        b (int): The blue component of the color value.
        a (int): The alpha (transparency) component of the color value.
    '''
        
    def __init__(self, r: int, g: int, b: int, a: int):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __repr__(self):
        return (self.r, self.g, self.b, self.a)

    def __eq__(self, other):
        if isinstance(other, RGBA):
            return (self.r == other.r and self.g == other.g and
                    self.b == other.b and self.a == other.a)
        return False
    
    def __sub__(self, other):
        if isinstance(other, RGB):
            return RGBA(
                max(0, self.r - other.r),
                max(0, self.g - other.g),
                max(0, self.b - other.b),
                self.a
            )
        elif isinstance(other, RGBA):
            return RGBA(
                max(0, self.r - other.r),
                max(0, self.g - other.g),
                max(0, self.b - other.b),
                max(0, self.a - other.a)
            )
        elif isinstance(other, int):
            return RGBA(
                max(0, self.r - other),
                max(0, self.g - other),
                max(0, self.b - other),
                max(0, self.a - other)
            )
        elif isinstance(other, (int,int)):
            return RGBA(
                max(0, self.r - other[0]),
                max(0, self.g - other[0]),
                max(0, self.b - other[0]),
                max(0, self.a - other[1])
            )
        raise TypeError("Subtraction only supported between RGBA and RGB/RGBA/int or (int:rgb/int:alpha) instances")
    
    def __add__(self, other):
        if isinstance(other, RGB):
            return RGBA(
                min(255, self.r + other.r),
                min(255, self.g + other.g),
                min(255, self.b + other.b),
                self.a
            )
        elif isinstance(other, RGBA):
            return RGBA(
                min(255, self.r + other.r),
                min(255, self.g + other.g),
                min(255, self.b + other.b),
                min(255, self.a + other.a)
            )
        elif isinstance(other, int):
            return RGBA(
                min(255, self.r + other),
                min(255, self.g + other),
                min(255, self.b + other),
                min(255, self.a + other)
            )
        elif isinstance(other, tuple(int,int)):
            return RGBA(
                min(255, self.r + other[0]),
                min(255, self.g + other[0]),
                min(255, self.b + other[0]),
                min(255, self.a + other[1])
            )
        raise TypeError("Addition only supported between RGBA and RGB/RGBA/int or (int:rgb/int:alpha) instances")
    
    def __get_pydantic_core_schema__(self, handler):
        return core_schema.typed_dict_schema({
                'r': core_schema.typed_dict_field(core_schema.int_schema()),
                'g': core_schema.typed_dict_field(core_schema.int_schema()),
                'b': core_schema.typed_dict_field(core_schema.int_schema()),
                'a': core_schema.typed_dict_field(core_schema.int_schema()),
            })