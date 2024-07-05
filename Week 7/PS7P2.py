#FunctionType
def Batavcalc(Hits, Atbats):
  Batav = Hits / Atbats
  return Batav
#Input
Players = 0
Confirmation = input("Would you like to use this program? : ")
while Confirmation == "Yes":
  Lname = input("Enter Last Name: ")
  Hits = float(input("Enter Number of Hits: "))
  Atbats = float(input("Enter Number of At Bats: "))
  #Process
  Batav = Batavcalc(Hits, Atbats)
  #Output
  print("Last Name: ", Lname)
  print("Batting Average: ", Batav)
  Players = Players + 1
  Confirmation = input("Would you like to use this program again? : ")
print("Number of Players: ", Players)