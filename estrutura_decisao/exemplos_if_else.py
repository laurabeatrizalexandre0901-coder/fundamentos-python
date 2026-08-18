def aluno_aprovado():
    nota_1 = float(input("Qual a primeira nota do aluno? "))
    nota_2 = float(input("Qual a segunda nota do aluno? "))

    media = (nota_1 + nota_2) / 2

    if media >= 7:
        print("Aprovado")
     elif media >= 5 and media < 6:
        print("Aluno de recuperacao")
    else:
        print("Aluno de recuperacao")


aluno_aprovado()


