"""
6. Create a python file named sum_of_digits, Write a program that can return the sum of digits from a  string
             Ex:
                 input: A1B2C3

                 output: 6
"""


def sum_of_digits(word: str) -> int:
    result = 0
    for x in word:
        if x.isdigit():
            result += int(x)
    return result


print(sum_of_digits('A1B2C7'))

