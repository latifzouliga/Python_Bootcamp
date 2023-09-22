import collections


def display_palindrome(strings: list) -> str:
    def is_palindrome(st: str) -> bool:
        return st[::-1] == st

    max_length = 0
    result1 = ''
    for x in strings:
        if is_palindrome(x) and max_length < len(str(x)):
            max_length = len(str(x))
            result1 = str(x)
    return result1


list1 = ['ana', 'hi', 'layal', 'xuliga', 'racecar', 'aka']

result = display_palindrome(list1)
print(result)

print('---------------------------------------------------------')


def is_anagram(str_1: str, str_2: str) -> bool:
    return sorted(str_1) == sorted(str_2)


def group_anagrams(strs):
    answer = collections.defaultdict(list)
    for word in strs:
        answer[list(sorted(word))].append(word)
    return (answer.values())


list2 = group_anagrams(['cat', 'act', 'eat', 'ate'])
print(list2)
