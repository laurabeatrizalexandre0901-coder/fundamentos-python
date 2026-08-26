def adicionar_nome(nomes, nome):
    nomes.append(nome)
    return nomes


# Lista inicial
nomes = []

# Entrada do usuário
nome = input("Digite um nome: ")

# Chamada da função
adicionar_nome(nomes, nome)

# Exibir resultado
print("Lista de nomes:", nomes)