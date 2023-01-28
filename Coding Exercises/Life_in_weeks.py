# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

life_span_days= 90 * 365
life_span_weeks = 90 * 52
life_span_months=90 * 12
current_days = int(age)*365
current_weeks= int(age) * 52
current_months=int(age) * 12

print(f"You have {life_span_days - current_days} days, {life_span_weeks-current_weeks} weeks, and {life_span_months-current_months} months left")
