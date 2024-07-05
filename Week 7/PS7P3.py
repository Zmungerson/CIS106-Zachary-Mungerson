#Function
def MPGcalc(Miles, Gallons):
  MPG = Miles / Gallons
  return MPG
#Input
Entries = 0
Confirmation = input("Would you like to use this program? : ")
while Confirmation == "Yes":
  City = str(input("Enter Name of City"))
  Miles = float(input("Enter Number of Miles Driven: "))
  Gallons = float(input("Enter Number of Gallons Used: "))
  #Process
  MPG = MPGcalc(Miles, Gallons)
  #Output
  print("City: ", City)
  print("Miles: ", Miles)
  print("Miles Per Gallon: ", MPG)
  Entries = Entries + 1
  Confirmation = input("Would you like to use this program again? : ")
print("Number of Entries: ", Entries)