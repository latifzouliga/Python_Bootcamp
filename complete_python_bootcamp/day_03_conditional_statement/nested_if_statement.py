if height := int(input("How tall are you? ")) >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5")
    elif 12 < age < 15:
        print("Please pay $8")
    else:
        print("Please pay $12")
else:
    print("Sorry, you have to grow taller before you can ride")
