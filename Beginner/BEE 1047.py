HS, MS, HE, ME = map(int, input().split())  # Hora e minuto de início, hora e minuto final
# 1h = 60 min
dif = (HE * 60 + ME) - (HS * 60 + MS)  # Diferença em minutos
if dif <= 0:
    dif = dif + 24 * 60  # Adicionar o número de minutos em 1 dia caso troque o dia
hour = dif // 60  # Horas
min = dif % 60  # Resto serão minutos
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hour, min))
