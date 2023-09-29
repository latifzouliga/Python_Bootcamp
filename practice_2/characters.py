"""
5. Create a python file named characters, write a program that can retrieve the digits, letters and special characters
 from a string
            Ex:
                input:
                    mn@#123Ab!

                output:
                    letters: mnAb
                    digits: 123
                    special chars: @#!

"""


def retrieve_chars(string: str) -> None:
    digits = ''
    letters = ''
    special_chars = ''

    for c in string:
        if c.isdigit():
            digits += c
        elif c.isalpha():
            letters += c
        else:
            special_chars += c
    print(f'letters: {letters}\ndigits: {digits}\nspecial chars: {special_chars}')


retrieve_chars('mn@#123Ab!')
