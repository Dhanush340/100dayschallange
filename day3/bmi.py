height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / height**2
bmi2 = round(bmi, 2)
print("your BMI value is " + str(bmi2))
if bmi2<18.5:
    print("you are underweight")
elif bmi2<25:
    print("you have normal weight")
elif bmi2<30:
    print("you are overweight")
elif bmi2<35:
    print("you are obese")
else:
    print("you are clinically obese")

