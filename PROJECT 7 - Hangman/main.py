import hangman_art
import random

# Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Setup live counter
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# Create blanks
display = []
for _ in range(word_length):
    display += "_"

while True:
#prompt user to guess the letter
    guess = input("Guess a letter: ").lower()
    
# If the user has entered a letter they've already guessed, print the letter and let them know.  
    if guess in display:
        print(f"You've already guessed {guess}")
        
# Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

# Check if user is wrong.
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            print("You lose.\n")
            print(f"The Correct word is : {chosen_word}")
            break
    print(f"{' '.join(display)}\n")

# Check if user has got all letters.
    if "_" not in display:
        print("You win.")
        break

