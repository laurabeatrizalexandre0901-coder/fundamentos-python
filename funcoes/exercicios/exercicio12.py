def calcular_preco_final(preco, desconto):
    valor_desconto = preco * desconto / 100
    return preco - valor_desconto

preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite o percentual de desconto: "))

valor_final = calcular_preco_final(preco, desconto)

print("O valor final é: R$", valor_final)