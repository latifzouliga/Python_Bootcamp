"""
1.6 Write a program that can remove the duplicated elements from a list
				Ex:
					elements = [1,2,3,4,5,1,2,3,4,5]

					Output:
						[1, 2, 3, 4, 5]

					Notes: Do Not use Set
"""
# =====================================

elements = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
result = list(dict.fromkeys(elements))
print(result)

# =====================================

result2 = list()
for x in elements:
    if x not in result2:
        result2.append(x)

print(result2)

# =====================================

result3 = []
[result3.append(x) for x in elements if x not in result3]
print(result3)

# =====================================

result4 = list(sorted(set(elements), reverse=True))
print(result4)
