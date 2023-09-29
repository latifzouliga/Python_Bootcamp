"""
14. Create a python file named grade_level2.  write a program that asks user to enter the grade level number,
determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

                    For Any Other grade: Invalid grade level given

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

grade = int(input('Enter you grade\n'))

if 0 < grade <= 18:
    if grade <= 5:
        print('Elementary school')
    elif grade <= 8:
        print('Middle school')
    elif grade <= 12:
        print('High school')
    elif grade <= 16:
        print('College')
    else:
        print('grand School')
else:
    print("invalid")
