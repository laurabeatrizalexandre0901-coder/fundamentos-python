def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

imc = calcular_imc(peso, altura)

print("O IMC é:", imc)