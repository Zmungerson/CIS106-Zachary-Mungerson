#Input
Quantity = int(input("Enter Quantity of Item: "))
#Process
if Quantity > 10000: 
  Price = 10
elif Quantity > 5000:
  Price = 20
else:
  Price = 30
ExtPrice = Quantity * Price
Tax = ExtPrice * 0.07
Total = ExtPrice + Tax
#Output
print ("The Extended Price is: $", ExtPrice)
print ("The Tax is: $", Tax)
print ("The Total is: $", Total)