def converter_fahrenheit(celsius):
    return celsius * 1.8 + 32

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = converter_fahrenheit(celsius)

print("A temperatura em Fahrenheit é:", fahrenheit)