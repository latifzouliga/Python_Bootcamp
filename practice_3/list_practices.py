"""
1.1 Write a program that can move all the zeros to the last indexes of ArrayList
	            Ex:
	                list: [1,0,2,0,3,0,4,0]

	            output:
	                [1, 2, 3, 4, 0, 0, 0, 0]
"""

# shifted backwards (to left)
list1 = [1, 0, 2, 0, 3, 0, 4, 0]

for x in range(len(list1)):
    if list1[x] == 0:
        list1.append(list1.pop(x))
print(list1)


def swap(input: list, left: int, right: int):
    temp = input[left]
    input[left] = input[right]
    input[right] = temp


def swap_to_left(input: list):
    left = 0
    right = len(input) - 1

    while left < right:
        if input[left] > 0:
            if input[right] == 0:
                swap(input, left, right)
            else:
                while input[right] > 0:
                    right -= 1
                swap(input, left, right)

            right -= 1
        left += 1


list2 = [1, 0, 2, 0, 3, 0, 4, 0]

swap_to_left(list2)
print(list2)
