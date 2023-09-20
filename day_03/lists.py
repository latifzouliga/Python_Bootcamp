##

groceries_list = ['Eggs', 'Mild', 'Rice']

groceries_list.append('Chicken')

groceries_list.extend(('Beef', 'Orange', 'Onion'))

groceries_list[-2] = 'Apple'

print(len(groceries_list))
print(groceries_list)

print('========================================')

numbers_list = [10, 20, 30, 40, 50, 60, 70, 80]

print(numbers_list)

numbers_list[2:-2] = [3, 4, 5, 6]

print(numbers_list)

print('========================================')
# slicing

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

list1 = characters[2:-3]
print(list1)

list2 = characters[:4]
print(list2)

list3 = characters[2:]
print(list3)

characters[2:5] = ['Cydeo', 'Java', 'Python', 'C++', 'C']
print(characters)

names = ['Conor', 'Steve', 'Hazel', 'Breana']

for x in names:
    print(x)

print('========================================')

nums = [10, 20, 30, 40, 50, 60]

for n in range(len(nums)):
    nums[n] = nums[n] / 5

print(nums)

print('========================================')

nums = [10, 20, 30, 40, 50, 60]

for n in reversed(range(len(nums))):
    print(nums[n])

print('========================================')

for x in nums[::-1]:
    print(x)

print('========================================')

for x in reversed(nums):
    print(x)

print('================== while ======================')

i = 0

while i < len(nums):
    print(nums[i])
    i += 1

print('================ methods ========================')

nums = [100, 20, 39, 11, 5, 60]
# nums.sort()
nums.sort(reverse=True)
print(nums)

print('============ convert list to tuple and vice versa =============')

tuple_element = ('Java', 'Python', 'C#', 'Ruby')
print(tuple_element)

list_element = list(tuple_element)
list_element[-2] = 'C++'

print(list_element)

tuple_element = tuple(list_element)
print(tuple_element)

# memory allocation
# two object allocated in the memory even if they have the same exact content
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(list1 is list2)

# one memory allocation if there are the same element in tuples
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (1, 2, 3, 4, 5)
print(tuple1 is tuple2)

print('-------------- remove() --------------')

groceries_list = ['Eggs', 'Mild', 'Rice', 'Beef', 'Orange', 'Onion']
print(groceries_list)

groceries_list.remove('Eggs')
print(groceries_list)

print('-------------- pop() --------------')
groceries_list.pop(1)
print(groceries_list)

print('-------------- insert() --------------')
groceries_list.insert(2, 'Chicken')
print(groceries_list)

print('-------------- index  --------------')
print(groceries_list.index('Chicken'))

print('-------------- count --------------')
nums = [1, 2, 3, 4, 5, 1, 1, 1, 1, 1]
print(nums.count(1))

print("======================================= Comprihansion")

nums = []
for x in range(1, 50):
    nums.append(x)

print(nums)

print('-----------------------')

"""
divisible_by_5 = []

for x in nums:
    if x % 5 == 0:
        divisible_by_5.append(x)

print(divisible_by_5)

"""

new_list = [x for x in nums if x % 5 == 0]
print(new_list)

print('-----------------------')

even_nums = [x for x in nums if x % 2 == 0]
odd_nums = [x for x in nums if x % 2 == 1]

print(even_nums)
print(odd_nums)

print('-----------------------')

names = ['Python', 'Java', 'Java', 'JavaScript', 'java', 'JaVA', 'Ruby']

names = [x for x in names if x.lower() != 'java']

print(names)




