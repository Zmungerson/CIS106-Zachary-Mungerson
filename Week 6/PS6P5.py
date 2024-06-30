with open("PS6/PS6P5.txt", "r") as txt:
  Lname = str(txt.readline().rstrip('/n'))
  TuitionTotal = 0
  StudentTotal = 0
  while Lname != "":
    State = str(txt.readline().rstrip('/n'))
    CrPrice = 250 if State == "I" else 500 
    Credit = float(txt.readline().rstrip('/n'))
    Tuition = CrPrice * Credit
    TuitionTotal = TuitionTotal + Tuition
    StudentTotal = StudentTotal + 1
    print("Last Name:", Lname)
    print("Credits Taken:", Credit)
    print("Tuition Owed: $", Tuition)
    Lname = str(txt.readline().rstrip('/n'))
  print("Total Tuition Owed: $", TuitionTotal)
  print("Total Students: ", StudentTotal)
    