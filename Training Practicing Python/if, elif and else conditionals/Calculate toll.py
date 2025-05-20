# Programa para calcular o valor do pedágio

# Entrada da distância
distancia = float(input("Digite a distância percorrida (em km): "))

# Verificação do valor do pedágio
if distancia <= 100:
    pedagio = 10.00
elif distancia <= 200:
    pedagio = 20.00
else:
    pedagio = 30.00

# Saída do resultado
print(f"Para {distancia} km, o valor do pedágio é: R$ {pedagio:.2f}")
