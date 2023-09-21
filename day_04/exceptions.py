try:
    num = 10 / 0
    print(num)
except ZeroDivisionError:
    print('Something went wrong')
else:
    print('Nothing went wrong')
finally:
    print('finally block')

print('Test Completed')

print('--------------------------------------------------')

tuple1 = (10, 20, 30, 40)
try:
    print(tuple1[2000])
except IndexError:
    print('Index Number Too Large')
else:
    print('The index number is valid')

print('--------------------------------------------------')

try:
    raise FileNotFoundError('No such file')
except SyntaxError:
    print('It is a syntax error')
except OSError:
    print('The problem is your OS')
except ArithmeticError:
    print('It is an arithmetic error')
finally:
    print('Finally block')

print('--------------------------------------------------')

