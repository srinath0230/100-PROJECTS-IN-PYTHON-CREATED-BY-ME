import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)
print(f"Psst, the correct answer is {number}")

level = input("Choose a difficulty. Type 'easy' or 'hard': ")
easy_lives = 3
hard_lives = 5

def life_count(guessed_number):
    while condition:
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number:
            condition = False
            return ("You Win!")
        elif guessed_number != number:
            easy_lives = easy_lives - 1
            return easy_lives
    

    
    
if level == "easy":
    print(f"You have {easy_lives} attempts remaining to guess the number.")
    condition = True
    while condition and easy_lives > 0:
        guessed_number = int(input("Make a guess: "))
        if guessed_number == number:
                condition = False
                print("You Win!")
                exit()
        elif guessed_number != number:
            easy_lives = easy_lives - 1
            if guessed_number > number :
                print("Too high")
                if easy_lives != 0:
                    print("Guess again.")
                    print(f"You have {easy_lives} attempts remaining to guess the number.")
            elif guessed_number < number : 
                print("Too low")
                if easy_lives != 0:
                    print("Guess again.")
                    print(f"You have {easy_lives} attempts remaining to guess the number.")

    print("You've run out of guesses, you lose.")

                

