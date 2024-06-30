#Input
Number = 0
Fibo1 = 1
Fibo2 = 1
Fibo3 = 1
#Process/Output
while Number < 20:
  print(Fibo3)
  Number = Number + 1
  Fibo3 = Fibo1
  Fibo1 = Fibo2 + Fibo1 
  Fibo2 = Fibo3