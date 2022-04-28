import random

nameAsCSV = input("Give everybody's Names, separated by comma: ")
names = nameAsCSV.split(", ")

num_ityems = len(names)
choice = random.randint(0, num_ityems - 1)
payBill = names[choice]
# payBill = random.choice(names)
print(f"{payBill} will pay the bill today")
