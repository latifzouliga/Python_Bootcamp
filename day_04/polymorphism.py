from day_03.abstraction2 import Shape, Square, Rectangle
from day_03.encapsulation1 import Person

# with polymorphism, we can restrict the type

shape1: Shape = Square(5)

shape2: Shape = Rectangle(5, 4)


def display_area(shape: Shape):
    print(f'{shape.name} \'area is {shape.area()}')


display_area(shape1)
display_area(shape2)


person = Person('James', 35)

# exception
display_area(person)
