# -*- coding: utf-8 -*-

segundos_total = int(input())

horas = segundos_total//(60*60)
minutos = (segundos_total-(horas*(60*60)))//60
segundos = segundos_total-((horas*60*60)+(minutos*60))

print('{}:{}:{}'.format(horas, minutos, segundos))
