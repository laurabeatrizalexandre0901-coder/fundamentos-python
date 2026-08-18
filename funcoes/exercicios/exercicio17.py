def trocar_valores(a, b):
    print("Antes:")
    print("A =", a)
    print("B =", b)

    a, b = b, a

    print("\nDepois:")
    print("A =", a)
    print("B =", b)


a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))

trocar_valores(a, b)