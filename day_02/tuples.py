# size of tuple can not be changed
# the element can not be updated
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(type(days))
print(len(days))

print(days[0])
print(days[-1])

# slicing

work_days = days[1:4]
print(work_days)

week_days = days[:-1]
print(week_days)

weekend = days[-3:]
print(weekend)

# ==: same value
# is: same object

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

# merge
new_tuple = tuple1 + tuple2
print(new_tuple)

# multipy
tuple3 = tuple1 * 3
print(tuple3)

# reverse
print(days[::-1])

reversed_tuple = tuple(reversed(days))
print(reversed_tuple)

# tuple has only 2 methods are: index() and count()

print(days.index('Wednesday'))

numbers = (10, 10, 2, 3, 10, 10, 60, 10, 10, 10)
print(numbers.count(10))

for x in days:
    print(x)

for x in reversed(range(len(days))):
    print(x)

for x in range(-len(days), 0):
    print(x)

print('=============== nested tuple =============')
nested_tuple = ((1, 2, 3), (40, 50, 60), (700, 800, 900))

for x in nested_tuple:
    print(x)
    for each in x:
        print(each)



print('-------------------------')

for i in range(0, len(nested_tuple)):
    for j in range(0, len(nested_tuple[i])):
        print(nested_tuple[i][j])


print(nested_tuple[:1])