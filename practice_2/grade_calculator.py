"""
8. Create a python file named grade calculator, and Write a program for grade calculator:
    8.1. Ask the user "Enter your score"
            If user enters invalid score, terminate the program after displaying the error message "Invalid Entry"

    8.2 Display the grade of the student.
                    90 ~ 100 ==> A
                    80 ~ 89 ==> B
                    70 ~ 79 ==> C
                    60 ~ 69 ==> D
                    0 ~ 59 ==> F

    8.3 Ask the user would you like to continue
            If "yes" --> repeat the previous steps
            If "no" --> print "Thank you for using Cydeo Grade Calculator APP"

            If user enters an invalid entry, ask the user to re-enter until user provides a valid entry
"""
import sys


def calculate_grads() -> None:
    def grades(grade: int) -> None:
        valid_grades = 0 < grade <= 100
        if valid_grades:
            if grade <= 59:
                result = 'F'
            elif grade <= 69:
                result = 'D'
            elif grade <= 79:
                result = 'C'
            elif grade <= 89:
                result = 'B'
            else:
                result = 'A'
        else:
            result = 'Invalid grade'
        print(result)

    try:
        grade = input('Enter your grade\n')
        grades(int(grade))
    except ValueError:
        print(f'Invalid Grade: \'{grade}\'', file=sys.stderr)

    while True:
        yes_no = input('Would you like to continue?\n')

        if yes_no.lower() == 'yes':
            try:
                grade = input('Enter your grade\n')
                grades(int(grade))
            except ValueError:
                print(f'Invalid Grade: \'{grade}\'', file=sys.stderr)
        elif yes_no.lower() == 'no':
            print("Thank you for using Cydeo Grade Calculator APP")
            break
        else:
            print('Enter Yes or No')


calculate_grads()


