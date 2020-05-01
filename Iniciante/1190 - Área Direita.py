# -*- coding: utf-8 -*-

operação = str(input())

indice = [

    23,
    34,  35,
    45,  46,  47,
    57,  56,  58,  59,
    67,  68,  69,  70,  71,
    79,  80,  81,  82,  83,
    92,  93,  94,  95,
    105, 106, 107,
    118, 119,
    131,
]

soma = 0
for a in range(0, 144):
    valor = float(input())
    if a in indice:
        soma += valor

if operação == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(indice)))
