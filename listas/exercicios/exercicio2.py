def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)
    return alunos


# Lista de alunos
alunos = ["Ana", "João", "Maria", "Carlos"]

# Entrada do usuário
nome = input("Digite o nome do novo aluno: ")
posicao = int(input("Digite a posição onde o aluno será inserido: "))

# Chamada da função
inserir_aluno(alunos, nome, posicao)

# Exibir resultado
print("Lista de alunos:", alunos)