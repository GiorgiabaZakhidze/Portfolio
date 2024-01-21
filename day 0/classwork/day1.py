

 

student_grade1 = int(input("შეიყვანე შენი ქულა: "))
student_grade2 = int(input("შეიყვანე შენი ქულა: "))
student_grade3 = int(input("შეიყვანე შენი ქულა: "))
student_grade4 = int(input("შეიყვანე შენი ქულა: "))

sum = student_grade1 + student_grade2 + student_grade3 + student_grade4 
average = sum / 4
if student_grade1 > 9:
  print("congrats for toaster")
elif student_grade2 > 5:
  print("congrats you escaped for matrix")
else:
  if student_grade3 < 0:
    print("There is something wrong with you")
  elif student_grade4 < 10:
    print("There is something wrong with you")



