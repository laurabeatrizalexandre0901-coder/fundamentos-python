# Laço for simples
import time


def mostrar_numero():
    for i in range (1, 6):
        print(f"o numero é {i}")
        time.sleep(5)

    # Mostrar_numero

def mostrar_numero_alterado():
    for num in range (0, 20, 2):
        print(f"o numro atual e {num}")

mostrar_numero_alterado()


mostrar_numero()

def somar_numeros():
    total = 0
    for valor in range(1, 20):
        total += valor
    print(total)


somar_numeros()