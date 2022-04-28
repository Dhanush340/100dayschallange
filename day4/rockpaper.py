import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
selection = [rock, paper, scissors]
# f"{row1}\n{row2}\n{row3}\n"
# print(selection)
choose =int(input("what do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors: "))

print('Computer choose:')
computer_choose = random.randint(0,2)
print(selection[computer_choose])

if choose >= 3 or choose<0:
    print("you typed an invalid number, you lose!")
elif choose == 0 and computer_choose == 2:
    print("you win")
elif computer_choose == 0 and choose == 2:
    print("you lose")
elif computer_choose > choose:
    print('you lose')
elif choose> computer_choose:
    print("you win")
elif computer_choose == choose:
    print("draw")

