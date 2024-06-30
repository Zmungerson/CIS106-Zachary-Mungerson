#Input
with open("PS6/PS6P4.txt", "r") as txt:
  Item = str(txt.readline().rstrip('/n'))
  TotalPrice = 0
  TotalQuant = 0
  Extprice = 0
  #Process
  while Item !="":
    Quantity = float(txt.readline().rstrip('/n'))
    Price = float(txt.readline().rstrip('/n'))
    Extprice = Quantity * Price
    TotalPrice = TotalPrice + Extprice
    TotalQuant = TotalQuant + Quantity
    #Output
    print("Item:", Item)
    print("Quantity:", Quantity)
    print("Price: $", Price)
    print("Extended Price: $", Extprice)
    Item = str(txt.readline().rstrip('/n'))
  AvPrice = TotalPrice / TotalQuant
  print("Total Price: $", TotalPrice)
  print("Total Quantity:", TotalQuant)
  print("Average Price: $", AvPrice)
    