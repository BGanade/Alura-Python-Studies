limite = 3000
despesas = float(input("Digite o total de despesas do mes (R$): "))

if despesas > limite:
    print("Você gastou mais do que o limite estipulado")
else:
    print("Você está dentro do orçamento :-)")
