def idade():
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("de Menor")
    else:
        print("de Maior")


idade()