#Operador or

def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("vc tem dinheiro pra comprar? "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"Vou comer um MC hj? {autorizado}")

posso_comprar()