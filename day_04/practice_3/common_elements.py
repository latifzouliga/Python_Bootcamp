"""
1.5 Write a program that can display the common elements of two lists:
				Ex:
					list1 = [1,2,3,4,5]
					list2 = [4,5,6,7,8]

					Output:
						4
						5
"""
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(list1)
print(list2)
for x in list1:
    for y in list2:
        if x == y:
            print(x)

list3 = list1 + list2
print(list3)

list4 = set(list1) & set(list2)
print(list4)

list1 = ['little', 'blue', 'widget']
list2 = ['there', 'is', 'a', 'little', 'blue', 'cup', 'on', 'the', 'table']

list3 = set(list1) & set(list2)
print(list3)
