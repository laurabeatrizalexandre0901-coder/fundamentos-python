def compra():
    compra = float(input("Digite o valor da compra: "))

    if compra <= 100:
        frete = 20
    elif compra <= 300:
        frete = 10
    else:
        frete = 0

    total = compra + frete

    print("Valor da compra: R$", compra)
    print("Valor do frete: R$", frete)
    print("Valor total: R$", total)


compra()