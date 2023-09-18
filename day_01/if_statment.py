if True:  # the start of the block
    print('Python Programming')

print('Java Programming')

print('--------------------------------------------------')

score = 70

# in Python, we can not leave the block empty
if score >= 60:
    pass  # allows to go to next line without giving a code fragment

if score >= 60:
    print('Congrats! you passed the exam')

s = 'Hello World!'
if 'H' and 'H' in s:
    print(s, 'has', 'H and W')

print('--------------------------------------------------')

if score >= 60:
    print('Passed')
else:
    print('Not Passed')

print('--------------------------------------------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not Eligible'

print(result)

print('--------------------------------------------------')
# ternary
age = 26
result = 'Eligible' if age >= 21 else 'Not Eligible'
print(result)

# multi-branch-if statement

print('--------------------------------------------------')

num = 100
result = None

if num > 0:
    result = 'Positive'
elif num < 0:
    result = 'Negative'
else:
    result = 'Zero'

print(result)

print('--------------------------------------------------')

score = 30

if 0 <= score <= 100:
    if score >= 60:
        print('Passed')
    else:
        print('Failed')
else:
    print("Invalid Score")

print('--------------------------------------------------')

score = -700

if 0 <= score <= 100:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')
else:
    print('Invalid Score')
