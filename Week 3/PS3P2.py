#Input
Item = input( "Item: " )
Quantity = float(input("Enter Quantity of Item: "))
#Process
Price = 10 if Item == "A" else 20
ExtPrice = Quantity * Price
#Output
print("Item: ", Item)
print("Quantity: ", Quantity)
print("The total Price is $: ", ExtPrice)