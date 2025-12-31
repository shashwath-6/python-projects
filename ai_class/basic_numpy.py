def calculate_gpa():
  grade={
      "A":4.0,
      "B":3.0,
      "C":2.0,
      "D":1.0,
      "F":0.0
  }
  total_course = int(input("Enter your course: "))
  total_credit=0
  total_gpa=0
  for i in range(total_course):
    print("Enter your course no",i+1)
    enter_grade = input("Enter your grade: ").strip().upper()
    while(enter_grade not in grade):
      enter_grade = input("Enter your grade: ").strip().upper()
    credit = int(input("enter the credit for this course: "))
    avg=grade[enter_grade]
    total_gpa += avg*credit
    total_credit += credit
  if total_credit==0:
    return "Invalid credit score"
  else:
    gpa = total_gpa/total_credit
    return gpa

gpa = calculate_gpa()
print("Your GPA is:", gpa)