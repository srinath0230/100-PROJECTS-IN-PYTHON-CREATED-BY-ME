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

# created a list and optimised the problem instead of using if-else statement

game_images = [rock,paper,scissors]

# prompt user for input
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# checks the conidition if the user enter valid number
if user_input >= 0 and user_input <= 2:  
  print(game_images[user_input])
# computer chose is random
  computer_chose = random.randint(0,2)
  print(f"computer chose: {game_images[computer_chose]}") 
# checks the rules of the game and declear winner
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
# if condition fails / invaild input 
else:
  print("Invalid number,You Lose!")
