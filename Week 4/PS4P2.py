#Input
Part = input("Enter Part Number: ")
Quantity = int(input("Enter Quantity of Parts: "))
#Process
if Part == "10" or Part == "55":
 Price = 1.00
elif Part == "99":
 Price = 2.00
elif Part == "80" or Part == "70":
 Price = 3.00
else:
 Price = 5.00
Total = Quantity * Price
#Output
print ("Part Number: ", Part)
print ("Price per Part: $", Price)
print ("Total Price: $", Total)