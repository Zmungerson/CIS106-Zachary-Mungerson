#Input
Ticker = input("Enter Ticker Symbol: ")
Price = float(input("Enter Price Per Share: "))
Quantity = float(input("Enter Quantity of Shares: "))
#Process
Investment = Price * Quantity
#Output
print(Ticker)
print("The Total Investment is $", Investment)