def calcular_conta(consumo, preco_kwh):
    return consumo * preco_kwh

consumo = float(input("Digite o consumo em kWh: "))
preco_kwh = float(input("Digite o preço do kWh: "))

valor_conta = calcular_conta(consumo, preco_kwh)

print("O valor da conta é: R$", valor_conta)