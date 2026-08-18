def cadastro():
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    profissao = input("Digite a profissão: ")
    cidade = input("Digite a cidade: ")

    print("\n======= CADASTRO =======")
    print("Nome:", nome)
    print("Idade:", idade, "anos")
    print("Profissão:", profissao)
    print("Cidade:", cidade)
    print("========================")


cadastro()