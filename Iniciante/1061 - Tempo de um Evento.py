# -*- coding: utf-8 -*-

from datetime import datetime

dia_inicio = int(str(input()).split()[1])
horario_inicio = str(input()).replace(' : ', ' ').split()
hora_inicio = int(horario_inicio[0])
min_inicio = int(horario_inicio[1])
seg_inicio = int(horario_inicio[2])

data_inicial = str(dia_inicio)+' '+str(3)+' '+str(2000) + \
    ' '+str(hora_inicio)+' '+str(min_inicio)+' '+str(seg_inicio)
data_inicial = datetime.strptime(data_inicial, "%d %m %Y %H %M %S")

dia_final = int(str(input()).split()[1])
horario_final = str(input()).replace(' : ', ' ').split()
hora_final = int(horario_final[0])
min_final = int(horario_final[1])
seg_final = int(horario_final[2])

data_final = str(dia_final)+' '+str(3)+' '+str(2000)+' ' + \
    str(hora_final)+' '+str(min_final)+' '+str(seg_final)
data_final = datetime.strptime(data_final, "%d %m %Y %H %M %S")


data = str(data_final - data_inicial).replace(' days,',
                                              '').replace(':', ' ').replace('day,', '').split()

if len(data) == 3:
    dia = int(0)
    hora = int(data[0])
    minuto = int(data[1])
    segundo = int(data[2])
else:
    dia = int(data[0])
    hora = int(data[1])
    minuto = int(data[2])
    segundo = int(data[3])
print('''{} dia(s)
{} hora(s)
{} minuto(s)
{} segundo(s)'''.format(dia, hora, minuto, segundo))
