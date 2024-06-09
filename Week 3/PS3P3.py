#Input
Quantity = float(input( "Total Number of Books: " ))
Price = float(input("Price Per Book $: "))
#Process
Extprice = Quantity * Price
Shipping = 0 if Extprice >50 else 25
Total = Extprice + Shipping
#Output
print("The Total Price is $", Total)
print("The Price of Shipping is $", Shipping)