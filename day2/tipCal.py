print("welcome to the tip calculator.")
bill = input("what was the total bill? $")
percentage = input("what percentage tip would you like to give? 10, 12, 15? ")
people = input("how many people to split the bill? ")

# tipaspercent = percentage/100
# totaltip= bill * tipaspercent
# totalBill = bill+totaltip

final_pay = (float(bill) / int(people)) * ((int(percentage)/100) + 1)
bill_with_tip = round(final_pay, 2)
print(f"Each person should pay: ${bill_with_tip}")



