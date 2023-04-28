print("Digite a base e a altura do retângulo")
b = float(input())
h = float(input())
a = b * h
p = 2 * (b + h)
d = (b**2 + h**2)**0.5
print(f"Área = {a:.2f} - Perímetro = {p:.2f} - Diagonal = {d:.2f}")