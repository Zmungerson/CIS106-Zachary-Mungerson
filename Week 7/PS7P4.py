def Ratecalc(Code):
  Payrate = 50 if Code == "J" else 30 if Code == "A" else 25
  return Payrate
#Input
Total = 0
Confirmation = input("Would you like to use this program? : ")
while Confirmation == "Yes":
  Lname = input("Enter Last Name: ")
  Code = input("Enter Job Code: ")
  Hours = float(input("Enter Number of Hours Worked: "))
  #Process
  Payrate = Ratecalc(Code)
  Gross = Payrate * Hours
  Total = Total + Gross
  #Output
  print("Last Name: ", Lname)
  print("Gross Pay: $", Gross)
  Confirmation = input("Would you like to use this program again? : ")
print("Total Gross Pay: $", Total)