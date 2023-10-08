"""
1.8  Write a program that can display the unique elements of a list:
					ex:
						list = [1, 1, 2, 3, 3, 4, 5, 5]

					output:
						[2, 4]
"""
list1 = [1, 1, 2, 3, 3, 4, 5, 5]

result = []

for x in list1:
    count = 0
    for y in list1:
        if x == y:
            count += 1

    if count == 1:
        result.append(x)

print(result)

my_dict = dict()

for key, value in enumerate(list1):
    my_dict[value] = key

print(my_dict)

import numpy as nm

print(nm.unique(list1))

from collections import Counter

keys = list(Counter(list1).keys())
values = list(Counter(list1).values())
lista = zip(keys, values)

dic = {k: v for k, v in zip(kies, values)}
print(f'dict {dic}')

print(keys)
print(values)
