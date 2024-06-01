#Input
Lname = input("Enter Last Name: ")
Midterm = float(input("Enter Midterm Score: "))
Final = float(input("Enter Final Score: "))
#Process
Midterm2 = Midterm * .40
Final2 = Final * .60
ExamPoints = Midterm2 + Final2
#Output
print(Lname)
print("The Total Exam Points are", ExamPoints)