# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name3 = name1 + name2


t = int(name3.lower().count("t"))
r = int(name3.lower().count("r"))
u = int(name3.lower().count("u"))
e = int(name3.lower().count("e"))
l = int(name3.lower().count("l"))
o = int(name3.lower().count("o"))
v = int(name3.lower().count("v"))
e = int(name3.lower().count("e"))

sum1 = t+r+u+e
sum2 = l+o+v+e

total = str(sum1) + str(sum2) 

if int(total) < 10 or int(total) > 90:
    print(f"Your score is {total}, you go together like coke and mentos")
elif int(total) > 40 and int(total) < 50:
    print(f"Your score is {total}, you are alright together.") 
else:
    print(f"Your score is {total}.") 
