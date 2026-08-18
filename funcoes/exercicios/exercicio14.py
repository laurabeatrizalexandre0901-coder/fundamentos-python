def calcular_consumo(distancia, combustivel):
    return distancia / combustivel

distancia = float(input("Digite a distância percorrida (km): "))
combustivel = float(input("Digite a quantidade de combustível (L): "))

consumo = calcular_consumo(distancia, combustivel)

print("O consumo médio é:", consumo, "km/L")