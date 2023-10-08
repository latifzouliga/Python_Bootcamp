"""
 1.2 write a program that can multiply each odd number by 2
		            ex:
		            	list = [1,2,3,4,5];

		                output: [2,2,6,4,10]
"""

list1 = [1, 2, 3, 4, 5]
list1 = list(map(lambda x: x * 3, list1))

print(list1)

nums = [1, 2, 3, 4, 5]

for x in range(0, len(nums) - 1):
    nums[x] = nums[x] * 2

print(nums)
nums = [1, 2, 3, 4, 5]
nums = [x * 4 for x in nums]

print(nums)
