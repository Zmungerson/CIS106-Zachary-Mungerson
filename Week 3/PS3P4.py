#Input
Name = input("Appliance: ")
Cost = float(input("Cost of Appliance : $"))
#Process
WarrantyDec = 0.1 if Cost > 1000 else 0.05
WarrantyPrice = Cost * WarrantyDec
Total = Cost + WarrantyPrice
#Output
print("Appliance: ", Name)
print("Cost of Appliance: $", Cost)
print("Cost of Warranty: $", WarrantyPrice)
print("Total Cost: $", Total)
