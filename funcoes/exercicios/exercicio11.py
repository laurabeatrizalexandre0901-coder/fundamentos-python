def calcular_salario(valor_hora, horas):
    return valor_hora * horas

valor_hora = float(input("Digite o valor da hora trabalhada: "))
horas = float(input("Digite a quantidade de horas trabalhadas: "))

salario = calcular_salario(valor_hora, horas)

print("O salário é: R$", salario)