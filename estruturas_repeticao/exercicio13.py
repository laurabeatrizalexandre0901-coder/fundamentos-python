def mostrar_primos(inicio, fim):
    for numero in range(inicio, fim + 1):
        contador = 0

        for i in range(1, numero + 1):
            if numero % i == 0:
                contador += 1

        if contador == 2:
            print(numero)


inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

mostrar_primos(inicio, fim)