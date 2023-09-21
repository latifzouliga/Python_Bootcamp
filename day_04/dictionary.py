employee1 = {}

employee1['name'] = 'James'
employee1['name'] = 'Daniel'
employee1['age'] = 45
employee1['salary'] = 60_000

print(employee1)

employee2 = {
    'name': 'James',
    'age': 29,
    'salary': 90_000,
    'full_time': False
}

print(employee2)
print(employee2['name'])

employee2['salary'] += 10000
print(employee2)

employee2.update({'age': 33})
print(employee2)

employee2['full_time'] = True
# employee2.update({'full_time': True})
print(employee2)

employee2.pop('full_time')
print(employee2)

l = employee2.copy()
print(l)

# print(help(dict.popitem))

print(employee2.popitem())  # removes the last pair

print(employee2.keys())
print(employee2.values())

print('=============== iterating dictionary')

employee3 = {
    'name': 'Shay',
    'age': 29,
    'salary': 110_000,
    'full_time': False,
    'job_title': 'Developer',
    'company': 'cydeo'
}

print(list(employee3.keys()))

for key in employee3.keys():
    print(f'{key} : {employee3[key]}')

print('--------------------------------')

values = list(employee3.values())
print(values)

for value in employee3.values():
    print(values)

print('-------------')
values1 = [value for value in employee3.values()]
print(values1)

print('-------------items-------------------')
# returns a collection of tuple
tuples = [x for x in employee3.items()]
print(tuples)

for x in employee3.items():
    print(f'{x[0]} : {x[1]}')

print('--------------------------------')

students = {
    'A01': {
        'name': 'James',
        'gender': 'Male',
        'gpa': 3.5,
        'subject': ('Math', 'Physics')

    },
    'A02': {
        'name': 'hazel',
        'gender': 'Female',
        'gpa': 3.8,
        'subject': ('Biology', 'Programming')
    },
    'A03': {
        'name': 'Yulia',
        'gender': 'Female',
        'gpa': 4,
        'subject': ['Chemistry', 'Programming']

    }
}
print(students)

students['A01']['gpa'] = 4

print(students)

students['A02'].update({'name': 'Daniel', 'gender': 'Male'})

print(students)

students['A03']['subject'][1] = 'Biology'

print(students['A03'])

print('--------------------------------')

for x in students.items():
    print(x[1])
    for y in x[1]:
        print(y)

print('--------------------------------')

for value in students.values():
    for y in value.values():
        print(y)