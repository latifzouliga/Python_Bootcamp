"""
18. Create a python file named grade, a variable named grade is given. write a program to print the following messages:
            'A': excellent
            'B': great job
            'C': good
            'D': passed
            'F': failed
            other wise: invalid

            NOTE: MUST USE NESTED IF. DO NOT USE MORE THAN ONE PRINT STATEMENT
"""
grade = 'H'
is_valid = grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'F'
result = ''

if is_valid:
    if grade == 'A':
        result = 'Excellent'
    elif grade == 'B':
        result = 'Great Gob'
    elif grade == 'C':
        result = 'good'
    elif grade == 'D':
        result = 'Passed'
    else:
        result = 'Failed'
else:
    result = 'Invalid'

print(result)