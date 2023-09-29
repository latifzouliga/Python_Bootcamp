"""
9. Create a python file named birthday and create the following variable
             name, birthDay, birthMonth, birthYear

             use concatenation to display the birthday of the person

                 if  name = "John"
                     birth_day = 25
                     birth_month = "April"
                     birth_year = 1995;

                 output:
                     John was born on April/25/19
"""

name = "John"
birth_day = 25
birth_month = "April"
birth_year = 1995

print(f'{name} was born on {birth_month}/{birth_day}/{str(birth_year)[:-2]}')