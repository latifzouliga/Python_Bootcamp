# Welcome to the tip calculator
# What was the total bill?
# What percentage tip would you like to give? 10, 12, or 15?
# How many people to split the bill?
# Each person should pay: $

print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
num_of_people = int(input("How many people to split the bill? "))
calc_tip = bill * (tip / 100)
bill += calc_tip
bill /= num_of_people
print(f"Each person should pay: ${round(bill, 2)}")
