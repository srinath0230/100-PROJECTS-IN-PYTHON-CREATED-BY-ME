#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# used shuffle function to shuffle the order of lists 
random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

print("Eazy Level Password - Order not randomised: ", end= "")
# This code print first letters then sybmbols and at the end numbers which is little predictable
for i in range(0,nr_letters):
    print(letters[i], end = "")
for j in range(0,nr_symbols):
    print(symbols[j], end = "")
for k in range(0,nr_numbers):
    print(numbers[k], end = "")
print()


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

random.shuffle(letters)
random.shuffle(numbers)
random.shuffle(symbols)

# created a new list so that it can store all(numbers ,symbols,letters) together.
list = []
print("Hard Level Password - Order of characters randomised: ", end = "")
# using for loop appended all the characters in new list
for i in range(0,nr_letters):
    list.append(letters[i])
for j in range(0,nr_symbols):
    list.append(numbers[j])
for k in range(0,nr_numbers):
    list.append(symbols[k])
#using shuffle all the characters are now shuffled and are now randomised)
random.shuffle(list)
# To calculate length of all character and use in the range function
total = nr_letters+nr_symbols+nr_numbers
# converting list into string
for l in range(0,total):
    print(list[l], end ="")
       
