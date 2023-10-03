"""
10. Create a python file named tuples_practices:
        10.1 Write a program that can display the palindrome strings from a tuple of string

                Ex:
                    words = ('Java', 'Anna', 'python', 'Cydeo', 'Level')

                    output:
                        Anna
                        Level


        10.2 Write a program that can display the common elements of two lists:

                Ex:
                    tuple1 = (1,2,3,4,5)
                    tuple2 = (4,5,6,7,8)

                    Output:
                        4
                        5


        10.3 Write a program that can count the even and odd number from a tuple of integers

                Ex:
                    numbers = (1, 2, 3, 4, 5, 6, 7)

                    Output:
                        There are 3 even numbers and 4 odd numbers

"""

words = ('Java', 'Anna', 'python', 'Cydeo', 'Level', 'Racecar')


def palindrome(word: tuple) -> list:
    def is_palindrome(w: str) -> bool:
        w = w.lower()
        return w == w[::-1]

    palindromes = list()
    for x in word:

        if is_palindrome(x):
            palindromes.append(x)

    return palindromes


list_of_palindromes = palindrome(words)
print(list_of_palindromes)

print('----------------------------')


def common_elements(t1: tuple, t2: tuple):
    print('(', end=' ')
    for x in t1:
        for y in t2:
            if x == y:
                print(x, end=' ')
    print(')', end='')
    print()


tuple1 = (1, 2, 3, 4, 5, 9)
tuple2 = (4, 5, 6, 7, 8, 9)

common_elements(tuple1, tuple2)


print('----------------------------')


def count_evens_and_odds(tup: tuple) -> None:
    evens = 0
    odds = 0

    for x in tup:
        if x % 2 == 0:
            evens += 1
        else:
            odds += 1

    print(f'There are {evens} even numbers and {odds} odd numbers')


numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
count_evens_and_odds(numbers)
