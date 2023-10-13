"""
1.7 Write a program that can remove string elements from a list if the first and last characters of the string are same
				ex:
					list = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}

				output:
					["Lan", "Ebrahim", "Farida"]
"""

list1 = {"Anna", "Canada", "Bob", "David", "Lan", "Abida", "Ebrahim", "Farida"}
result = []
for x in list1:
    if x[0].lower() == x[-1].lower():
        result.append(x)

print(result)
# =======================================

list2 = [x for x in list1 if x[0].lower() == x[-1].lower()]
print(list2)

