pi = 3.14159
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
tr = (A * C) / 2
c = pi * (C * C)
tra = ((A + B) * C) / 2
q = B * B
r = A * B
print("TRIANGULO: %0.3f" %tr)
print("CIRCULO: %0.3f" %c)
print("TRAPEZIO: %0.3f" %tra)
print("QUADRADO: %0.3f" %q)
print("RETANGULO: %0.3f" %r)