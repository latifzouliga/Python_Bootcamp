print("======================== break ==================")

for i in range(1, 6):
    print(i)
    if i == 3:
        break


print("======================== continue ==================")

for i in range(1, 6):
    if i == 3 or i == 4:
        continue
    print(i)

print("======================== pass ==================")

for i in range(1, 6):
    if i == 3 or i == 4:
        pass
    print(i)

def function():
    pass

if True:
    pass

