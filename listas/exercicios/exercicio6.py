def encontrar_produto(produtos, produto):
    return produtos.index(produto)


produtos = ["Arroz", "Feijão", "Macarrão", "Leite", "Café"]
produto = input("Digite o produto que deseja encontrar: ")
posicao = encontrar_produto(produtos, produto)
print("O produto está na posição:", posicao)

encontrar_produto(produtos, produto)

