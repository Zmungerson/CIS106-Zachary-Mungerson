#Input
Make = input("Enter Make of Car: ")
Model = input("Enter Model of Car: ")
MSRP = float(input("Enter MSRP of Car: "))
DiscountP = float(input( "Enter Discount Percent: "))
#Process
DiscountD = DiscountP / 100
DiscountA = DiscountD * MSRP
Dprice = MSRP - DiscountA
#Output
print(Make)
print(Model)
print("The MSRP is $", MSRP)
print("The Discount Amount is $", DiscountA)
print("The Discounted Price is $", Dprice)
