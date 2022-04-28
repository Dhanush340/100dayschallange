height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height)**2
print(bmi)
bmi2 = round(bmi)
print("your BMI value is " + str(bmi2))
