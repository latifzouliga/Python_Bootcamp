"""
13.  Create a python file named grade_level1.  write a program that asks user to enter the grade level number,
 determine and print which school type the person is in is in.
            grade level and types are:
                    1-5: Elementary school
                    6-8: Middle school
                    9-12: High school
                    13-16: College
                    17-18: Grad School

              Assume that the given number is 1 ~ 18
"""

grade = int(input("Enter your grade\n"))

result = ''
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

print(result)
