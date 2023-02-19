#My own code without using fuction
import random
import art

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f"Psst, the correct answer is {number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if level == "easy":
    lives = 10
else:
    lives = 5
    
print(f"You have {lives} attempts remaining to guess the number.")
condition = True
while condition and  lives > 0:
    guessed_number = int(input("Make a guess: "))
    if guessed_number == number:
            condition = False
            print("You Win!")
            exit()
    elif guessed_number != number:
        lives = lives - 1
        if guessed_number > number :
            print("Too high")
            if lives != 0:
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")
        elif guessed_number < number : 
            print("Too low")
            if lives != 0:
                print("Guess again.")
                print(f"You have {lives} attempts remaining to guess the number.")

print("You've run out of guesses, you lose.")
