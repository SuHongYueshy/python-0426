import math

print(math.pi)


class Circle():

    pi = 3.14

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def area(self):
        return math.pi * self.r * self.r


c = Circle(1, 2, 3)
print(Circle.pi)
c2 = Circle(4, 5, 6)

print(hasattr(c, 'x'))
print(hasattr(c, 'y'))

print(getattr(c, 'x'))
print(getattr(c, 'y'))
print(getattr(c, 'z', 'not found,'))

setattr(c, 'z', 4)
print(getattr(c, 'z'))

print(hasattr(c, 'area'))
print(getattr(c, 'area'))

fn = getattr(c, 'area')
print(fn())

c.pi = 4
print(c.pi)
print(Circle.pi)