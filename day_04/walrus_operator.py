# walrus operator was introduced in payton 3.8
# it assigns value to variable as part of a larger expression

# foods = list()
#
# while True:
#     food = input('Enter your favorite food: ')
#     if food == 'quit':
#         break
#     foods.append(food)
#
# print(foods)

# let re-write the above code using walrus operator

foods = list()

while food :=  input('Enter your favorite food: ') != 'quit':
    foods.append(food)

print(foods)