from datetime import datetime, timedelta

entrada = input()

hr_inicial, min_inicial, hr_final, min_final = map(int, entrada.split())

dt_inicial = datetime(2023, 1, 1, hr_inicial, min_inicial)
dt_final = datetime(2023, 1, 1, hr_final, min_final)

dt_duracao = dt_final - dt_inicial
hr_duracao = dt_duracao.seconds // 3600
min_duracao = (dt_duracao.seconds // 60) % 60

if min_duracao < 0:
    hr_duracao -= 1
    min_duracao = 60 + min_duracao
elif hr_duracao < 1 and min_duracao < 1:
    hr_duracao = 24
    min_duracao = 0 

print("O JOGO DUROU {} HORA(S) E {} MINUTO(S)".format(hr_duracao, min_duracao))
