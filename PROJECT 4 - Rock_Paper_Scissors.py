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

#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
if user_input == 0:
  print(rock)
elif user_input == 1:
  print(paper)
elif user_input == 2:
  print(scissors)

print("computer chose: " )
computer_chose = random.randint(0,2)

if computer_chose == 0:
  print(rock)
elif computer_chose == 1:
  print(paper)
elif computer_chose == 2:
  print(scissors)

if user_input == 0 and computer_chose == 1:
  print("You Lose!")
elif user_input == 1 and computer_chose == 2:
  print("You Lose!")
elif user_input == 2 and computer_chose == 0:
  print("You Lose!")
elif user_input == computer_chose:
  print("Draw!")
else:
  print("You Win!")
