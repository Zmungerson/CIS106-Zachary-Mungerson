#1
List = []
Inputnum = int(input("Enter the Number of Items: "))
for _i in range(0, Inputnum):
  Num = int(input("Enter Number: "))
  List.append(Num)
print(List)
#2
List.insert(0, 99)
print(List)
#3  
List[0] = 100
print(List)
#4
List2 = [500, 600, 700, 800, 900]
List.extend(List2)
print(List)
#5
List.remove(800)
print(List)
#6
del List[2]
print(List)
#7
List3 = ["A", "B", "C", "A", "A", "C"]
#8
print(List3.count("A"))
#9
print(List3.index("B"))
#10
if "F" in List3:
  print("F is in the list")
else:
  print("F is not in the list")
#11
List2.clear()
print(List2)
#12
del List2
#print(List2)
#13
List4 = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
#14
List4.sort()
print(List4)
#15
players2 = List4
print(players2)
#16
players2.reverse()
print(List4)
print(players2)