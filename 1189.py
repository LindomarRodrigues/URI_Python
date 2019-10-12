# -*- coding: utf-8 -*-

operação = str(input())

matriz = []
for a in range(0, 12 * 12):
    valor = float(input())
    matriz.append(valor)
indices = [12,
           24,  25,
           36,  37,  38,
           48,  49,  50,  51,
           60,  61,  62,  63,  64,
           72,  73,  74,  75,  76,
           84,  85,  86,  87,
           96,  97,  98,
           108, 109,
           120,
           ]
total = 0
for a in indices:
    total += matriz[a]

if operação == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/len(indices)))
