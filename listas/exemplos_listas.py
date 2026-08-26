def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome} ")

Lista_de_nomes = ["Sophia", "Laura", "Mayara"]
mostrar_nomes(Lista_de_nomes)

#funcionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(Lista_de_nomes, "sara")


# Adicionado novo nome em uma posição específica
def adicionar_nome_posicao(nomes,nome,posicao ):
    nomes.insert(posicao,nome)
    print(f"O nome {nome} foi inserido na posição {posicao} na lista: {nomes}")

adicionar_nome_posicao(Lista_de_nomes,"nicolas", 2)


# juntando Duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")

novos_nomes = ["sosoh", "David"]
juntar_nomes(Lista_de_nomes, novos_nomes)

# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome n existe")
    else:
        nomes.remove(nome)
    print(f"O nome {nome} foi removido na lista: {nomes}")

remover_nome_pelo_valor(Lista_de_nomes, "sosoh")

# Removendo nome pela indice
def remover_nome_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} é {nomes[posicao]}, foi removido")

remover_nome_indice(Lista_de_nomes, 4)

# descobrindo a posição (index) pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome n existe")
    else:
        posicao = nomes.index(nome)
    print(f"A posição do nome {nome} é {posicao}")

encontrar_posicao_pelo_valor(Lista_de_nomes, "sosoh")

# contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"Quantidade de nomes: {quantidade}")

quantidade_de_nomes(Lista_de_nomes)


# ordenando os elementos da lista
def ordernar_nomes(nomes):
    lista_de_nomes_ordenados =  sorted(nomes, reverse=True)
    print(f"A lista ordenada é {lista_de_nomes_ordenados}")

ordernar_nomes(Lista_de_nomes)

# Operações matemáticas
# calcular média
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A media das notas é {media}")

notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, sophia = gerenciar_notas(notas_semestre,3.5)
print(f"notas_ordenadas = {notas_ordenadas}")
print(f"a nota das medias é = {sophia}")

# Lista de Listas
def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f"minha lista de produtos: {produtos[0][2]}")


lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50]
]
novo_produtos = ["Café", 2, ]
adicionar_produto(lista_produtos, novo_produtos)

def quantidade_total_produtos(produtos):
    quantidade = []

    for produto in produtos:
        print(f"rodando laço for em lista_produtos: {produto}")
        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"quantidade de produtos: {quantidade_produtos}")

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valores.append(produto[2])

    return sum(valores)
valor_total_produtos=valor_total_produtos(lista_produtos)
print(f"valor total: {valor_total_produtos}")





















