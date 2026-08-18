# Operador and

def pode_dirigir():
    idade = int(input("Digite a idade "))
    TEM_HABILITACAO = True

    autozido = idade >= 18 and TEM_HABILITACAO

    print(f"Usuário pode dirigir? {autozido}")

pode_dirigir()