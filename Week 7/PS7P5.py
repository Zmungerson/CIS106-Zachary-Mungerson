#Function 
def Tuitioncalc (Code, Hours): 
  Rate = 250 if Code == "I" else 550 
  Tuition = Rate * Hours  
  return Tuition
#Input
Total = 0
Confirmation = input("Would you like to use this program? : ")
while Confirmation == "Yes":
  Lname = input("Enter Last Name: ")
  Code = input("Enter District Code: ")
  Hours = float(input("Enter Number of Credit Hours: "))
  #Process
  Tuition = Tuitioncalc (Code, Hours)
  Total = Total + Tuition
  #Output
  print("Last Name: ", Lname)
  print("Tuition: $", Tuition)
  Confirmation = input("Would you like to use this program again? : ")
print("Total Tuition: $", Total)