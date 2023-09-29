"""
1.Create a python file named functions_practices:
    1.1 Create a function that can check if a person is eligible to vote
                Ex:
                    eligibleToVote(19, "USA");

                output:
                    You are not eligible to vote!

    1.2 Create a function that can calculate the grade of the student based on the score

    1.3 Create a function that can if the given integer is positive, negative or zero

    1.4 Create a function that can check if a string is palindrome, the function
    should return true if the given string is palindrome.
"""


# ========== is eligible to vote ============
def is_eligible_to_vote(age: int, country: str) -> bool:
    return 17 < age < 150 and country.upper() == 'USA'


print(is_eligible_to_vote(19, 'Usa'))


# ========== grade calcualator ===============
def grade_calculator(grade: int) -> str:
    result = ''
    if 0 < grade < 22:
        if grade <= 5:
            result = 'Elementary school'
        elif grade <= 8:
            result = 'Middle School'
        elif grade <= 12:
            result = 'High School'
        elif grade <= 16:
            result = 'College'
        elif grade <= 18:
            result = 'Grand School'
    else:
        result = 'Invalid Grade'
    return result


print(grade_calculator(-18))


# ================ palindrome ===================

def is_palindrome_1(word: str) -> bool:
    word = word.lower()
    return word[::-1] == word


print(is_palindrome_1('Ana'))


def is_palindrome_2(word: str) -> bool:
    word = word.lower()
    result = ''
    for x in reversed(word):
        result += x
    return result == word


print(is_palindrome_2('racecar'))


