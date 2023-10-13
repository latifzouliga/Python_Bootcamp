# Write a Python program to import a built-in array module and display the namespace of the said module.

import array

for name in array.__dict__:
    print(name)

print('---------------------------------')


# Write a Python program to create a class and display the namespace of that class.
class Employee:
    pass


for name in Employee.__dict__:
    print(name)

print('---------------------------------')


# Write a Python program to create an instance of a specified class and display the namespace of the said instance.

class Car:
    def __init__(self, name, brand, color):
        self.name = name
        self.brand = brand
        self.color = color


car = Car('Honda', 2021, 'Black')

print(car.__dict__)

'''prints:  {'name': 'Honda', 'brand': 2021, 'color': 'Black'}
'''

for name in car.__dict__:
    print(name)

''' prints:
__module__
__dict__
__weakref__
__doc__
'''

import builtins

help(builtins.abs)
print(builtins.abs(-232))
