# arithmetic: + - * / %

print(10 + 2)
print(10 - 2)
print(10 * 2)

# division always gets float
print(10 / 2)
# int, because we cast it int
print(int(10 / 2))

# shorthand assignment: = += -=
a = 100
a = 200
print(a)

a += 50
print(a)

a -= 50
print(a)

a /= 50
print(a)

# logical operator: and, or, not
# and for grouping element
# in: like contains in Java
s = 'Hello World'
print('H' and 'W' in s)

print(True and True)
print(True or False)

s = 'Java Python C# C++'
print('Java' or 'Ruby' in s)

age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'
print(is_eligible)


has_java = 'Java' in s
print(has_java)

print('Python' not in s)

print(not False)
print(not True)

# identity operators

print('==========================================')

# verify if two variables are referencing to the same objects (in Java we use == operator)
s1 = 'Java'
s2 = 'Java'
print(s1 is s2)
print(s1 == s2)