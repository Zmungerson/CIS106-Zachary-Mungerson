#Input
Quantity = float(input("Enter Quantity of Item: "))
#Process
Price = 5 if Quantity < 1000 else 3
ExtPrice = Quantity * Price
Tax = ExtPrice * 0.07
Total = ExtPrice + Tax
#Output
print("Quantity: ", Quantity)
print("The Price is: $", Price)
print("The Extended Price is: $", ExtPrice)
print("The Tax is: $", Tax)
print("The Total is: $", Total)