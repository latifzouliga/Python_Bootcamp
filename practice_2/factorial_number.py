"""
4. Create a python file named factorial_number, Write a program that can return the factorial number of any given number

            Ex:
                input: 5
                output: 120

                    ( because: 5! = 5 * 4 * 3 * 2* 1 = 120 )
"""


def factorial_num(number: int) -> int:
    result = 1
    for x in range(1, number + 1):
        result *= x
    return result


print(factorial_num(5))
