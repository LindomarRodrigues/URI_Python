# -*- coding: utf-8 -*-

valor = float(input())

if 0 <= valor <= 25:
    intervalo = '[0,25]'
elif 25 < valor <= 50:
    intervalo = '(25,50]'
elif 50 < valor <= 75:
    intervalo = '(50,75]'
elif 75 < valor <= 100:
    intervalo = '(75,100]'
else:
    print('Fora de intervalo')
    quit()

print('Intervalo {}'.format(intervalo))
