#Input
with open("PS6/PS6P3.txt", "r") as txt:
  Lname = str(txt.readline().rstrip('/n'))
  Bsum = 0
  #Process
  while Lname != "":
    Salary = float(txt.readline().rstrip('/n'))
    if Salary >= 100000:
      Brate = 0.2
    elif Salary >= 50000:
      Brate = 0.15
    else:
      Brate = 0.1
    Bonus = Salary * Brate
    Bsum = Bsum + Bonus
    #Output
    print(Lname, "Salary: $", Salary, "Bonus: $", Bonus)
    Lname = str(txt.readline().rstrip('/n'))
  print("Total Bonus: $", Bsum)