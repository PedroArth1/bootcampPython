# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
num_height = 0
total_heights = 0
for height in student_heights:
    num_height += 1
    total_heights += height
print(round(total_heights/num_height))



