# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

sentence = name1.lower() + name2.lower()
t = sentence.count('t')
r = sentence.count('r')
u = sentence.count('u')
e = sentence.count('e')

total1 = t+r+u+e
T1= str(total1)

l = sentence.count('l')
o = sentence.count('o')
v = sentence.count('v')
e = sentence.count('e')

total2 = l+o+v+e
T2 = str(total2)
loveScore = T1+T2
score = total1 + total2

if (score<10) or (score>90):
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif (score>=40) and (score<=50):
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")



