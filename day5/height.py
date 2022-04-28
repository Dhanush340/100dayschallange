# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
# print(student_heights)
total = 0
num_students = 0
for height in student_heights:
  total += height
  num_students+=1

#print(total)
#print(num_students)
avg_height = total/num_students
print(f"avarage height in classs is {round(avg_height, 2)}")
# Write your code below this row 👇



