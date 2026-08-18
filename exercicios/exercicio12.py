def login():
    senha = input("Digite sua senha: ")

    if senha == "python123":
        print("Acesso permitido")
    else:
        print("Senha inválida")

login()