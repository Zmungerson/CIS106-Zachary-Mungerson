#Input
Lname = input("Enter Last Name: ")
Dependent = float(input("Enter Number of Dependents: "))
Gross = float(input("Enter Gross Income: "))
#Process
AdjGross = Gross - (Dependent * 12000)
TaxR = 0.2 if AdjGross > 50000 else 0.1
TaxAmount = AdjGross * TaxR
if TaxAmount < 0:
    TaxAmount = 100
#Process
print(Lname)
print("Number of Dependents: ", Dependent)
print("Gross Income: $", Gross)
print("Adjusted Gross Income: $", AdjGross)
print("Total Tax Owed: $", TaxAmount)
