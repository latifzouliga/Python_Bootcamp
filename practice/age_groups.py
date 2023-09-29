"""
19. Create a python file named age_groups, write a program that asks user to enter their age and define the age
groups of the user
            age groups are:
                    Teenager (< 21)
                    Adult   (>=21 && <55 )
                    Senior  ( > 55 )

             if age is negative or greater than 150, print invalid

             NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""

age = 29
if 0 < age < 150:
    if age < 21:
        print('Teenager')
    elif age < 55:
        print('Adult')
    else:
        print('Senior')
else:
    print('Invalid age')
