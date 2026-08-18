def calcular_perimetro(base, altura):
    return 2 * (base + altura)

base = float(input("Digite a base: "))
altura = float(input("Digite a altura: "))

perimetro = calcular_perimetro(base, altura)

print("O perímetro é:", perimetro)