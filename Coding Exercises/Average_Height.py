# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
index = 0
add = 0
for _ in student_heights:
    add = add + student_heights[index]
    index = index+1
    if index >= len(student_heights):
        break
    else:
        continue
average = add / index
print(round(average))
