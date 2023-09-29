"""
21. Create a python file named number_to_words, Write a program that can convert user entered number (from 0~9)
to words.

    NOTE: MUST use ternary
"""
number = str(3453453)
word_digits = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

result = ''
for x in range(len(number)):
    print(f'{number[x]} {word_digits[int(number[x])]}')
