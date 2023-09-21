import json
import csv
from pandas import read_csv

path = 'files/Test.json'

jason_file = open(path, 'r')

dictionary = json.load(jason_file)

print(dictionary)

for x in dictionary:
    print(f'{x} : {dictionary[x]}')

jason_file.close()

print('======================= convert dict to json and saving it in a file ================')

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

my_file = open('files/Test_2.json', 'w')

students_file = json.dumps(students, indent=4)

my_file.write(students_file)

my_file.close()
my_file = open('files/Test_2.json', 'r')

loaded_file = json.load(my_file)

for x in loaded_file:
    print(f'{x} : {loaded_file[x]}')


for x in loaded_file:
    print(x)
    for y in loaded_file[x]:
        print(f'{y} : {loaded_file[x][y]}')

    print()


# my_file = open('files/Test_2.json', 'w')
#
# j_object = json.dumps(students, indent=4)  # converting dict to json object
#
# my_file.write(j_object)
