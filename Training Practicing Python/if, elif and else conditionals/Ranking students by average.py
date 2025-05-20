nota1 = float(input("Insira a primeira nota do aluno: "))
nota2 = float(input("Insira a segunda nota do aluno: "))
nota3 = float(input("Insira a terceira nota do aluno: "))

media = (nota1 + nota2 + nota3)/3

print(f"A media foi de {media}")

if media < 5:
    print("Reprovado")
elif 5 <= media < 7:
    print("Recuperação")
else:
    print("Aprovado")
