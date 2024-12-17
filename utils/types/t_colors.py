
class RGB:
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

class RGBA:
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