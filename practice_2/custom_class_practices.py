"""
9. Create a python file named custom_class_practices:
        9.1 Create a custom class named Pizza:
        Attributes:
            size, numberOfCheeseTopping, numberOfPepperoniTopping

            Add a constructor that can set all the fields

        Actions:
            calcCost(): returns the totalCost of the pizza
            __str__():returns a String containing the pizza size, quantity of each topping, and the pizza cost as calculated by calcCost()

        Pizza cost is determined by:
                        S: $10 + $2 per topping
                        M: $12 + $2 per topping
                        L: $14 + $2 per topping
"""
import sys


class Pizza:
    def __init__(self, size: str, num_of_cheese_toppings: int, num_of_pepperoni_toppings: int):
        self.size = size
        self.num_of_cheese_toppings = num_of_cheese_toppings
        self.num_of_pepperoni_toppings = num_of_pepperoni_toppings

    def calc_cost(self) -> int:
        total = 0
        if self.size == 'S' or self.size == 'M' or self.size == 'L':
            if self.size == 'S':
                total += 10 + (2 * self.num_of_pepperoni_toppings)
            elif self.size == 'M':
                total += 12 + (2 * self.num_of_pepperoni_toppings)
            else:
                total += 14 + (2 * self.num_of_pepperoni_toppings)
        else:
            print(f'Invalid Pizza size \'{self.size}\'', file=sys.stderr)

        return total

    def __str__(self):
        return f'{type(self).__name__} {self.__dict__} \'total:\' ${self.calc_cost()}'


pizza1 = Pizza('S', 2, 2)
pizza2 = Pizza('M', 2, 2)
pizza3 = Pizza('L', 2, 2)
pizza4 = Pizza('K', 2, 2)

# print(pizza1)
# print(pizza2)
# print(pizza3)
# print(pizza4)

"""
9.2 Create a class named Circle:
                Attributes:
                    instance: radius
                    static: pi

                Add a constructor that can set All the fields (instances)

                Actions:
                    calcArea(): returns the area of Circle

                    calcPerimeter(): returns the perimeter of Circle

                    __str__(): displays the radius, diameter, pi, area and perimeter of the circle when the object of
                    circle is passed in the print statement
"""

import math


class Circle:
    pi = math.pi

    def __init__(self, radius: int):
        self.radius = radius

    def calc_area(self) -> float:
        return round((self.pi * self.radius * self.radius), 2)

    def calc_perimeter(self) -> float:
        return round((2 * self.pi * self.radius), 2)

    def __str__(self) -> str:
        return f'{type(self).__name__} {self.__dict__} \'area:\' {self.calc_area()} \'perimeter:\' {self.calc_perimeter()}'


circle = Circle(3)
print(circle)
