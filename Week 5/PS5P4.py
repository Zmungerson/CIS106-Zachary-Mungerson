#Input
Confirmation = input("Would you like to use this program? : ")
#Process
Employees = 0
TotalGross = 0
AvGross = 0
while Confirmation == "Yes":
  Lname = input("Enter Last Name: ")
  Hours = float(input("Enter Hours Worked: "))
  Rate = float(input("Enter Hourly Rate: $"))
  Gross = (40 * Rate +
     (Hours - 40) * (Rate * 1.5)
     if Hours > 40
     else (Hours * Rate))
  Employees = Employees +1
  TotalGross = TotalGross + Gross
  AvGross = float(TotalGross / Employees)
  print(Lname)
  print("Gross Pay: $", Gross)
  Confirmation = input("Would you like to use this program again? : ") 
#Output
print("Total Gross Pay: $", TotalGross)
print("Average Gross Pay: $", AvGross)
print("Number of Employees: ", Employees)