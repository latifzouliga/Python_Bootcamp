"""
3. Create a python file named sum_of_even_odd:
        3.1 Write a program that can return the sum of even numbers between 1 to 100

        3.2 Write a program that can return the sum of odd numbers between 1 to 100

        3.3 write a program that can calculate the sum of all numbers between 1 to any given number
            ex:
                input: 100
                output: 5050

                input: 50
                output: 1275
"""


def sum_of_even_nums(number: int) -> int:
    sum_of_evens = 0

    for x in range(1, number + 1):
        if x % 2 == 0:
            sum_of_evens += x
    return sum_of_evens


print(sum_of_even_nums(100))


def sum_of_odd_nums(number: int) -> int:
    sum_of_odds = 0
    for x in range(1, number + 1):
        if x % 2 != 0:
            sum_of_odds += x
    return sum_of_odds


print(sum_of_odd_nums(50))
