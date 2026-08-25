def mostrar_pares(numero):
    for i in range(2, numero + 1, 2):
        print(i)
numero = int(input("Digite um número: "))
mostrar_pares(numero)