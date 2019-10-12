# -*- coding: utf-8 -*-

entrada = input().split()
x = float(entrada[0])
y = float(entrada[1])

if x > 0 and y > 0:
    quadrante = 'Q1'
elif x < 0 and y > 0:
    quadrante = 'Q2'
elif x < 0 and y < 0:
    quadrante = 'Q3'
elif x > 0 and y < 0:
    quadrante = 'Q4'
elif x == 0 and y != 0:
    quadrante = 'Eixo Y'
elif x != 0 and y == 0:
    quadrante = 'Eixo X'
elif x == 0 and y == 0:
    quadrante = 'Origem'

print(quadrante)
