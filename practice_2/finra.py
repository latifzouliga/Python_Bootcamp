"""
7. Create a python file named finra, Write a program which prints out the numbers from 1 to 100 but for numbers which
are a multiple of both 3 and 5, print "FINRA" instead of the number,  for numbers which are a multiple of 3,
print "FIN" instead of the number and for numbers which are a multiple of 5, print "RA" instead of the number.

    ex:
        output:
            1 2 FIN 4 RA FIN 7 8 FIN RA 11 FIN 13 14 FINRA 16 17 FIN
"""


def fin_firna(number: int) -> None:

    for x in range(number + 1):
        if x % 3 == 0 and x % 5 == 0:
            print('FIRNA', end=' ')
        elif x % 3 == 0:
            print('FIN', end=' ')
        elif x % 5 == 0:
            print('RA', end=' ')
        else:
            print(x, end=' ')
    print()


fin_firna(100)
