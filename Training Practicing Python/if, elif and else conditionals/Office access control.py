hora_atual = int(input("Digite o horario atual: "))
hora_minima_permitida = 8
hora_maxima_permitida = 18

if hora_minima_permitida <= hora_atual <= hora_maxima_permitida:
    print("Acesso Permitido.")
else:
    print("Acesso negado.")
