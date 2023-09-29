"""
2. Create a python file named numbers, Write a program that asks user to enter
number for 5 times, and print how many positive and negative numbers user entered
            Ex:
                Inputs:
                    10
                    20
                    -1
                    0
                    3

                Output:
                    3 positive and 1 negative
"""


def check_signed_numbers() -> None:
    nums = []
    for x in range(0, 5):
        nums.append(int(input('Enter a number\n----> ')))

    positive = 0
    negative = 0
    zeros = 0

    for n in nums:
        if n < 0:
            positive += 1
        elif n > 0:
            negative += 1
        else:
            zeros += 1

    print(f'{positive} positive, {negative} negative and {zeros} zero')


check_signed_numbers()
