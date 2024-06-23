#Input
Confirmation = input("Would you like to use this program? : ")
#Process
Users = 0
while Confirmation == "Yes":
  Lname = input("Enter Last Name: ")
  Exam1 = float(input("Enter Exam 1 Score: "))
  Exam2 = float(input("Enter Exam 2 Score: "))
  ExamAv = (Exam1 + Exam2) / 2
  Users = Users + 1
  #Output
  print("Last Name: ", Lname)
  print("Average Exam Score: ", ExamAv)
  print("User Amount: ", Users)
  Confirmation = input("Would you like to use this program again? : ")