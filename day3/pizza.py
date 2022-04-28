print("Welcome to the rollercoaster")
height = int(input("What is your height in cm? "))
bill = 0
if height > 120:
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print(f"you can ride and ticket is {bill}")
    elif age <= 18:
        bill = 7
        print(f"you can ride and ticket is {bill}")
    elif age >= 45 and age <= 55:
        print("you dont need to pay")
    else:
        bill = 12
        print(f"you can ride and ticket is {bill}")
photo = input("do you want photo? Y or N: ")

if photo == "Y":  # and (0 < age < 45 and age > 55)
    bill += 3
    print(f"total ticket  is {bill}")
