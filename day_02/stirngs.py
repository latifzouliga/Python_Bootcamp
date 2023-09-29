
# accessing string element using index
name = "Python"

print(len(name))
print(name[0])
print(name[len(name) -1])
print(name[-1])
print(name[-2])

# slicing

word = "Java Programming Language"
s1 = word[5:16]
print(s1)

s2 = word[:4]
print(s2)

s3 = word[::-1] # reverse the string after slicing
print(s3)

s4 = "Python Programming"
s5 = s4[7:]
print(s5)

print("==================================================")
s = "python programming language"
s = s.upper()
print(s)

s = s.capitalize()
print(s)

s = s.title()
print(s)

print('=============== strip ===================')
s = "      Python     "
s = s.lstrip()
print(s)

s = "      Python     "
s = s.rstrip()
print(s)

s = "      Python     "
s = s.strip()
print(s)

print('=============== index ===================')

s = "JAVA ABA"
print(s.index('A')) # indexof
print(s.rindex('A')) # lastIndexOf

s = "Java Java"

s = s.replace("Java", "Python")
print(s)

s = "Java Java Java"
s = s.replace("Java", "Python",1)
print(s)

s = "C# C# Python"
s = s.replace(" C#", " Java")
print(s)

s = "Java Java Java Python Python Java"
count_java = s.lower().count("java")
print(count_java)

count_python = s.count("Python")
print(count_python)

s1 = "java"
s2 = "JAVA"
print(s1.lower() == s2.lower())

s = "Java"
print(s[0].islower())
print(s[0].isupper())

s = "a"
print(s.isalpha())

s = "1"
print(s.isdigit())

s = "Cydeo School"
print(s.istitle())


word = 'python'
print(word.find('n')) # indexOf