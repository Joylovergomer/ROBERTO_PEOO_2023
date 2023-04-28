maior = 0
menor = 0
print("Digite três valores inteiros")
a = int(input())
b = int(input())
c = int(input())
if a < b and a < c:
  menor = a
if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = b
if a > b and a > c:
  maior = a
if b > a and b > c:
  maior = b
if c > a and c > b:
  maior = c
soma = maior + menor
print("A soma do maior com o menor número é ", soma)