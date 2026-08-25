def somar_ate(numero):
    soma = 0

    for i in range(1, numero + 1):
        soma += i

    return soma
numero = int(input("Digite um número: "))
resultado = somar_ate(numero)
print("A soma dos números de 1 até", numero, "é:", resultado)