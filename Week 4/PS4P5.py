#Input
Lname = input("Enter Last Name: ")
Salary = float(input("Enter Salary: $"))
JLevel = int(input("Enter Job Level: "))
#Process
if JLevel >= 10:
  BRate =0.25
elif JLevel >= 5:
  BRate = 0.20
else:
  BRate = 0.10
BAmount = BRate * Salary
#Output
print("Last Name: ", Lname)
print("Bonus Amount: $", BAmount)