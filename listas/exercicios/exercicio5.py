def remover_produto(produtos, produto):
    produtos.remove(produto)
    return produtos


produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]

produto = input("Digite o produto que deseja remover: ")

remover_produto(produtos, produto)

print("Lista de produtos:", produtos)