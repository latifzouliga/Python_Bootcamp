s = 'Python'
for each in s:
    print(each)

print("================================")

for i in range(0, len(s)):
    print(s[i])


print("=============== reverse =================")

for i in range(-len(s), 0):
    print(s[i])


print("=============== reverse =================")

for i in reversed(range(0, len(s))):
    print(s[i])