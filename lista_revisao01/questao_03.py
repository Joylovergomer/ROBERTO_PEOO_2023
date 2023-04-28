p = 0
i = 0
print("Digite quatro valores inteiros")
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a % 2 == 0):
  p = p + a
else:
  i = i + a
if (b % 2 == 0):
  p = p + b
else:
  i = i + b
if (c % 2 == 0):
  p = p + c
else:
  i = i + c
if (b % 2 == 0):
  p = p + d
else:
  i = i + d
print("Soma dos pares = ", p)
print("Soma dos ímpares = ", i)