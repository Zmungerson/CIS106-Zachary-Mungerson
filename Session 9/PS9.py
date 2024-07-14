#1
class Employee:
  def __init__(self, Fname, Lname, Salary, Brate):
    self.Fname = Fname
    self.Lname = Lname
    self.Salary = Salary
    self.Email = Fname + "." + Lname + "@company.com"
    self.Brate = Brate
  def Fullname(self):
    return '{} {}'.format(self.Fname, self.Lname)
  def Bonuscalc(self):
    Bonus = self.Salary * self.Brate
    return Bonus
Employee1 = Employee("John", "Doe", 50000, float(input("Enter Bonus Rate: ")))

Bonus = Employee1.Bonuscalc()
print(Bonus)
#2
class Student:
  def __init__(self, Fname, Lname, Code, Credits):
    self.Fname = Fname
    self.Lname = Lname
    self.Code = Code
    self.Credits = Credits
  def Tuitioncalc(self):
    Tuition = self.Credits*250 if self.Code == "I" else self.Credits*500
    return Tuition
Student1 = Student("Leo", "Valencia", "I", 15)
Student2 = Student("Steve", "Miller", "O", 5)

Tuition = Student1.Tuitioncalc()
print(Tuition)
Tuition = Student2.Tuitioncalc()
print(Tuition)