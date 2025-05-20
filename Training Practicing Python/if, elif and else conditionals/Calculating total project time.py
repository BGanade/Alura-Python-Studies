atividade_a = int(input("Digite a duracao da atividade a: "))
atividade_b = int(input("Digite a duracao da atividade b: "))
atividade_c = int(input("Digite a duracao da atividade c: "))
duracao = atividade_a + atividade_b + atividade_c

if (atividade_a or atividade_b or atividade_c) < 0:
    print("Erro: Os dias não podem ser negativos")
else:
    print(
        f"Os dias necessarios para fazer as atividades são de {duracao} dias ")
