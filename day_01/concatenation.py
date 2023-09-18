name = 'James'
age = 23

print('My name is ' + name)
# print('My age is '+ age) TypeError
print('My age is ' + str(age))

# we need to use placeholder if we want to concatenate two different datatypes
print('My age is {}'.format(age))

print('My name is {} and I am {} years old'.format(name, age))

print(f'My name is {name} and I am {age} years old')

# appending
print('Python', 3, 'is awesome: ', True)
