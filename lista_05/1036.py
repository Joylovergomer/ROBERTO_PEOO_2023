valores = input().split()
a = float(valores[0])
b = float(valores[1])
c = float(valores[2])
if a == 0 or b == 0 or c == 0:
  print("Impossivel calcular")
else:
  delta = ((b*b) - 4*a*c) **0.5
  if delta > 0:
    r1 = ((- b + delta) / (2*a))
    print("R1 = %0.5f" %r1)
    r2 = ((- b - delta) / (2*a))
    print("R2 = %0.5f" %r2)
  else:
    print("Impossivel calcular")