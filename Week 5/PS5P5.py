#Input
Confirmation = input("Would you like to use this program? : ")
#Process
TotalDiscount = 0
while Confirmation == "Yes":
  Price = float(input("Enter Price: $"))
  Quantity = float(input("Enter Quantity: "))
  ExtPrice = Price * Quantity
  DiscountPercent = 0.25 if ExtPrice > 10000 else 0.10
  DiscountAmount = ExtPrice * DiscountPercent
  TotalPrice = ExtPrice - DiscountAmount
  TotalDiscount = TotalDiscount + DiscountAmount
  print("Extended Price: $", ExtPrice)
  print("Discount Amount: $", DiscountAmount)
  print("Total Price: $", TotalPrice)
  Confirmation = input("Would you like to use this program again? : ")
#Output
print("Total Discount Amount: $", TotalDiscount)