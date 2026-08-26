def criar_ranking(pontuacoes):
    return sorted(pontuacoes, reverse=True)


pontuacoes = [150, 320, 250, 480, 190]

ranking = criar_ranking(pontuacoes)

print("Ranking:", ranking)