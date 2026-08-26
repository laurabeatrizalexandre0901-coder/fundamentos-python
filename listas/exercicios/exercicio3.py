def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)
    return convidados


convidados = ["Ana", "João", "Maria"]
novos_convidados = input("Digite os novos convidados separados por vírgula: ").split(",")
novos_convidados = [nome.strip() for nome in novos_convidados]
adicionar_convidados(convidados, novos_convidados)
print("Lista de convidados:", convidados)