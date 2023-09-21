from functools import reduce

print('---------------- closure -------------------')


# function inside another function

def display_message():
    def method():
        print('Hello World')
        print('I love python\n')

    method()
    method()
    method()
    method()


display_message()

print('--------------------------------')


def display_palindromes(strings: list):
    def is_palindrome(s: str) -> bool:
        return s[::-1].lower() == s

    for s in strings:
        if is_palindrome(s):
            print(s)


print('------------------- map -------------------')

nums = [10, 20, 30, 40, 50, 60, 70, 80]

nums = list(map(lambda x: x * 10, nums))

print(nums)

names = ('Java', "JAVA", 'java', 'Ruby', 'swift', 'CyDeO', 'javaSCRipt')

names = list(map(lambda x: str(x).upper(), names))
print(names)

dictionary = {'x': 100, 'y': 200, 'z': 300}

# TODO: FIX THIS
# dictionary = dict(map(lambda t: (t[0], t[1]) * 10, dictionary.items()))
# print(dictionary)

print('------------------- filter ------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# nums = [x for x in nums if x % 5 == 0]
nums = list(filter(lambda x: x % 5 == 0, nums))

print(nums)

names = ('Java', "JAVA", 'java', 'Ruby', 'swift', 'CyDeO', 'javaSCRipt')

# names = [s for s in names if not s.lower().startswith('j')]

names = list(filter(lambda s: not str(s).lower().startswith('j'), names))

print(names)

print('------------------- reduce ------------------')

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

result = reduce(lambda x, y: x + y, nums)
print(result)

list_1 = ['h', 'e', 'l', 'l', 'o']
print(reduce(lambda a, b: a + b, list_1))

list_2 = ['Java', 'Python', 'Ruby']
print(reduce(lambda x, y: f'{x} {y} and hello', list_2))
