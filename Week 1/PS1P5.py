#Input
Price = float(input("Enter Price of Item: "))
DiscountP = float(input("Enter Discount Percent: "))
#Process
DiscountD = DiscountP / 100
DiscountA = DiscountD * Price
Dprice = Price - DiscountA
#Output
print("Discount Amount: $", DiscountA)
print("Discounted Price: $", Dprice)