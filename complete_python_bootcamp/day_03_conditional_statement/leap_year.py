year = int(input("Enter a year"))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap")
#         else:
#             print(f"{year} is Not leap")
#     else:
#         print(f"{year} is a leap")
# else:
#     print(f"{year} is Not leap")

if (year % 400 == 0) and (year % 100 == 0):
    print("leap")
elif (year % 4 == 0) and (year % 100 != 0):
    print("leap")
else:
    print("not leap")

