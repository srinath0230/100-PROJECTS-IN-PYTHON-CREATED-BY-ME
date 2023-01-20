alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  # if statement is outside the for loop to avoid the error of constant changing from encode to decode
  if cipher_direction == "decode":
    # shift amount is minus 1 that means automatically goes back wards when user enters decode 
    shift_amount *= -1
    
  for char in start_text:
    # only alphabets are shifted by certain number and everything else is printed as it is
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
  print(f"Here's the {cipher_direction}d result: {end_text}")

# Imported and printed the logo from art.py when the program starts.(make sure to store both main and related files in same location)
from art import logo
print(logo)

# prompts the user until he ends the program
should_end = False
while not should_end:

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  # if user exceeds the number limit over 26 modulo helps to loop them through the alphabet from beginning 
  shift = shift % 26

  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
 # if user want to continue or end the program
  restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if restart == "no":
    should_end = True
    print("Goodbye")
    


