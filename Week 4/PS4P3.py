#Input
Princ = float(input("Enter Principal: $"))
Years = int(input("Enter Years to Maturity: "))
#Process
if Princ > 100000 and Years == 5:
  Rate = 0.06
elif Princ >= 50000 and Princ <= 100000 and Years == 10:
  Rate = 0.05
elif Princ >= 50000 and Princ <= 100000 and Years == 5:
  Rate = 0.04
else:
  Rate = 0.02
IntAmount = Rate * Princ
IntPer = Rate * 100
#Output
print("Principal: $", Princ)
print("Interest Rate: ", IntPer, "%")
print("Interest Amount: $", IntAmount)