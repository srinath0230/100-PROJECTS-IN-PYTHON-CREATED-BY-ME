############DEBUGGING#####################

# Describe Problem
def my_function():
  for i in range(1, 20):
    # bug range function includes 1 but excludes 20
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
#bug list out of range 
dice_num = randint(1, 6)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
# bug - when entered 1994 , include 1994
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994:
  print("You are a Gen Z.")

# Fix the Errors
age = input("How old are you?")
# bug string is not changed into int and str cannot be compared by int
if age > 18:
  # bug f string
print("You can drive at age {age}.")

#Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
# bug comparision operator is used in place of assignment 
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    # bug not indented inside for loop
  b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])
