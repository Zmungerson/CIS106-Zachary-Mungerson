#Input
Quantity = int(input("Enter Number of Tickets: "))
#Process
if Quantity >= 25:
  Price = 50
elif Quantity >= 10:
  Price = 60
elif Quantity >=5:
  Price = 70
else:
  Price = 75
Total = Quantity * Price
#Output
print("Number of Tickets: ", Quantity)
print("Price per Ticket: $", Price)
print("Total Price: $", Total)