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

print("=============== reverse =================")

result = ''
for x in s[::-1]:
    result += x
print(result)

print("================ while loop =================")

# num = int(input('Enter a Positive number\n'))
#
# while num <= 0:
#     num = int(input('Enter a Positive number\n'))
#
# print(f'You have entered: {num}')

print("=================================")

answer = input("Enter yes or No\n")

while not(answer.lower() == 'yes' or answer.lower() == 'no'):
    answer = input("Enter yes or No\n")

print(f'You have entered {answer}')