import numbers
from abc import ABC, abstractmethod

"""
abc: module name (builtin module)
ABD: Abstract class in abc module
abstractmethod: annotation that can be given to abstract methods
"""


# the recommended way to achieve abstraction
class Volume(ABC):
    @abstractmethod
    def volume(self):
        pass


class Shape(ABC):
    def __init__(self):
        self.name = type(self).__name__

    @abstractmethod  # make it must be implemented in sub-classes
    def area(self) -> numbers:
        pass

    def __str__(self):
        return f'{type(self).__name__}{self.__dict__}'


class Square(Shape, ABC):

    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self) -> numbers:
        return self.side * self.side


# TODO: COMPLETE THESE CLASSES
class Circle(Shape):
    def area(self) -> numbers:
        pass


class Rectangle(Shape):

    def area(self) -> numbers:
        pass


class Cube(Shape, Volume):
    def area(self) -> numbers:
        pass

    def volume(self):
        pass


class Cylinder(Shape, Volume):
    def area(self) -> numbers:
        pass

    def volume(self):
        pass


# =================================================
square1 = Square(3)
print(square1.area())

print(square1)


