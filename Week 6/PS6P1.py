#Input
Princ = float(input("Enter Principal: $"))
Rate = 1 + float(input("Enter Interest Rate:"))
#Process
Year = 0
TotalInt = 0
while Year < 5:
  Year = Year + 1
  Interest = Princ * Rate
  TotalInt = TotalInt + Interest - Princ
  #Output
  print("Year", Year, "Beginning Balance: $", Princ, "Ending Balance: $", Interest, )
  Princ = Interest
#Output
print("Total Interest: $", TotalInt)