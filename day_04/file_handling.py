import time
import os

desktop_path = '/Users/zouliga/Desktop/test.txt'
path = "files/Test.txt"
json_path = 'files/Test.json'

print('---------------------- read --------------------------------')
text_file = open(path, 'r')

print(text_file.read())  # reads the entire file
# print(text_file.readline())  # reads line by line
# print(text_file.readline())
# print(text_file.readline())
# print(text_file.readline())


print('---------------------- create and write --------------------------------')

path = 'files/test_create_fil.txt'

text_file_2 = open(path, 'w')

text_file_2.write('This is a new text file\nPython created this file')

for x in range(10):
    time.sleep(1)
    print(f'{x}\r')

print('--------------------------- remove ---------------------------')

os.remove('files/test_create_fil.txt')
