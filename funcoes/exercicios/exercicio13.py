def calcular_salario(salario_fixo, vendas, comissao):
    valor_comissao = vendas * comissao / 100
    return salario_fixo + valor_comissao

salario_fixo = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor das vendas: "))
comissao = float(input("Digite o percentual de comissão: "))

salario_final = calcular_salario(salario_fixo, vendas, comissao)

print("O salário final é: R$", salario_final)