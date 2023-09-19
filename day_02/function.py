# This is a function because it is outside a class
# Functions in python can return a value or can be void (generic fuction)
import numbers


def display_message():
    print("Hello Cydeo")
    print("It is Time to Learn Python")


display_message()


def value():
    return "Java is Better"


print(value())


# to make function a must to return a value
def return_int() -> int:
    return 10


print(return_int())


# restrict the datatype we pass to a function
def square(num: int):
    return num * num


print(square(10))


def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(10, 10))

print("=======================================================")


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 20, '+'))
print(calculate(100.5, 20.5, '/'))

print("=======================================================")


# default argument function
# method overloading

# we must pass 4 argument
def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    return n1 + n2 + n3 + n4


print(sum(10, 20))
print(sum(10, 20, 30))
print(sum(10, 20, 30, 40))

print(sum(10.5, 20.5))
