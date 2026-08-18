def calcular_idade(anos):
    meses = anos * 12
    dias = anos * 365

    print("Idade em meses:", meses)
    print("Idade em dias:", dias)

idade = int(input("Digite sua idade em anos: "))

calcular_idade(idade)