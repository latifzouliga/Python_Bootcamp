# # Data Types
#
# # String
#
# print("Hello"[0])
#
# print('123' + '345')
#
# # Integer
# print(123 + 345)
#
# a = 123
#
# print(type(a).__name__)
#
# num = input("Enter a number\n")
# print(int(num[0]) + int(num[1]))

print(3 * (3 + 3) / 3 - 3)

email = "zuuliga@gmail.com"
username, domain = email.split("@")

print(username)
print(domain)


# a = 3
# b = 10
#
# a, b = b, a
# print(a)
# print(b)

def div(a, b):
    return a / b


def smart_div(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
        return func(a, b)

    return inner


new_div = smart_div(div)
print(new_div(5, 10))
print(div(5, 10))

current_age = input()

weeks_in_one_year = 52

my_age = int(current_age) * weeks_in_one_year

age = 90 * weeks_in_one_year

print(age - my_age)

