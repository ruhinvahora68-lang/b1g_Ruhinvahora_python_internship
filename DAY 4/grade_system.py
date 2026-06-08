marks = int(input("Enter Marks: "))

if marks > 99:
  grade = "A+"
elif marks >= 90:
  grade = "A"
elif marks >= 75:
  grade = "B"
else:
  grade = "F"

print("Grade:", grade)
