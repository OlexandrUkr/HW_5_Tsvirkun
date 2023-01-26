class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x + other, self.y + other, self.z + other)
        elif isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise ValueError('Wrong input data format')

    def __mul__(self, other):
        if isinstance(other, int | float):
            return Vector(self.x * other, self.y * other, self.z * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y + self.z * other.z
        else:
            raise ValueError('Wrong input data format')

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"
