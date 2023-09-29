"""
7. Create a class named GallonsToLitters, Write a program that can convert gallon (int) to litter (double)
            Hints: 1 gallon = 3.79 litters
            Ex:
                Given Data:
                     gallon = 10

                output:
                    10 gallon is equal to 37.9 litters
"""

gallon = 10
letter = gallon * 3.785411784
print(f'{gallon} gallon is equal to {round(letter, 1)} litters')
