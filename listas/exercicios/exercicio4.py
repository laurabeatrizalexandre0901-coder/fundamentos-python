def remover_produto(produtos, produto):
    produtos.remove(produto)
    return produtos


# Lista de produtos
produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]

# Entrada do usuário
produto = input("Digite o produto que deseja remover: ")

# Chamada da função
remover_produto(produtos, produto)

# Exibir resultado
print("Lista de produtos:", produtos)