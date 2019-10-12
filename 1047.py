# -*- coding: utf-8 -*-

entrada = input().split()
hora_inicial = int(entrada[0])
minuto_inicial = int(entrada[1])
hora_final = int(entrada[2])
minuto_final = int(entrada[3])

if hora_inicial > hora_final:
    minutos = (24*60) - (((hora_inicial*60)+minuto_inicial) -
                         ((hora_final*60)+minuto_final))

elif hora_inicial == hora_final:
    minutos = 24*60
    if minuto_inicial == minuto_final:
        minutos = 24*60
    elif minuto_inicial > minuto_final:
        minutos -= minuto_inicial - minuto_final
    elif minuto_inicial < minuto_final:
        minutos = minuto_final - minuto_inicial

elif hora_inicial < hora_final:
    minutos = (((hora_final*60)+minuto_final) -
               ((hora_inicial*60)+minuto_inicial))

horas = 0
if minutos >= 60:
    horas = minutos // 60
    minutos = minutos - (horas * 60)
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(horas, minutos))
