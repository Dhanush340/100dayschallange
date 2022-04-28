# print("Welcome to the rollercoaster")
# height = int(input("What is your height in cm? "))
# if height > 120:
#     print("Can ride")
# else:
#     print("can't ride")

print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
if height > 120:
    age = int(input("What is your age? "))
    if age < 12:
        print("you can ride and ticket is $5")
    elif age <= 18:
        print("you can ride and ticket is $7")
    else:
        print("you can ride ticket is $12")
else:
    print("You can't ride")

