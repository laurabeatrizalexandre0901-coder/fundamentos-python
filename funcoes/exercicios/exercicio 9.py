def converter_para_centimetros(metros):
    return metros * 100

metros = float(input("Digite o valor em metros: "))

centimetros = converter_para_centimetros(metros)

print("O valor em centímetros é:", centimetros)