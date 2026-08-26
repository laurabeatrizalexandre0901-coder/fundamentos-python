def adicionar_nota(notas, nota):
    notas.append(nota)


def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)


def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)


def remover_nota(notas, nota):
    notas.remove(nota)


def remover_ultima_nota(notas):
    return notas.pop()


def encontrar_nota(notas, nota):
    return notas.index(nota)


def quantidade_notas(notas):
    return len(notas)


def ordenar_notas(notas):
    return sorted(notas)


def notas_invertidas(notas):
    return list(reversed(notas))


def somar_notas(notas):
    return sum(notas)


def media_turma(notas):
    return sum(notas) / len(notas)


notas = [7.5, 6.0, 8.5, 9.0, 5.5]

# 1. Adicionar uma nova nota
adicionar_nota(notas, 8.0)

# 2. Inserir uma nota em uma posição
inserir_nota(notas, 7.0, 2)

# 3. Adicionar várias notas
adicionar_varias_notas(notas, [6.5, 9.5])

# 4. Remover uma nota
remover_nota(notas, 5.5)

# 5. Remover a última nota
ultima = remover_ultima_nota(notas)

# 6. Encontrar a posição de uma nota
posicao = encontrar_nota(notas, 8.5)

# 7. Quantidade de notas
quantidade = quantidade_notas(notas)

# 8. Ordenar as notas
ordenadas = ordenar_notas(notas)

# 9. Mostrar notas em ordem inversa
invertidas = notas_invertidas(notas)

# 10. Soma das notas
soma = somar_notas(notas)

# 11. Média da turma
media = media_turma(notas)


print("Notas atuais:", notas)
print("Última nota removida:", ultima)
print("Posição da nota 8.5:", posicao)
print("Quantidade de notas:", quantidade)
print("Notas ordenadas:", ordenadas)
print("Notas em ordem inversa:", invertidas)
print("Soma das notas:", soma)
print("Média da turma:", media)