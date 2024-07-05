#Function
def Extpricecalc(Quantity, Price):
  Extprice1 = Quantity * Price
  Extprice2 = 0
  if Extprice1 >10000:
    Discount = Extprice1 * 0.10
    Extprice2 = Extprice1 - Discount
  else:
    Extprice2 = Extprice1
  return Extprice2
#Input
Extpricesum = 0
Confirmation = input("Would you like to use this program? : ")
while Confirmation == "Yes":
  Price = float(input("Enter price of item: $"))
  Quantity = float(input("Enter quantity of item: "))
  #Process
  Extprice2 = Extpricecalc(Quantity, Price)
  #Output
  print("Quantity: ", Quantity)
  print("Price: $", Price)
  print("Extended Price: $", Extprice2)
  Extpricesum = Extpricesum + Extprice2
  Confirmation = input("Would you like to use this program again? : ") 
print("Total Extended Price: $", Extpricesum)
