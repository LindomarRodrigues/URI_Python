# -*- coding: utf-8 -*-

opera��o = str(input())

matriz = []
for a in range(0, 12 * 12):
    valor = float(input())
    matriz.append(valor)
indices = [12,
           24, 25,
           36, 37, 38,
           48, 49, 50, 51,
           60, 61, 62, 63, 64,
           72, 73, 74, 75, 76, 77,
           84, 85, 86, 87, 88, 89, 90,
           96, 97, 98, 99, 100, 101, 102, 103,
           108, 109, 110, 111, 112, 113, 114, 115, 116,
           120, 121, 122, 123, 124, 125, 126, 127, 128, 129,
           132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142]
total = 0
for a in indices:
    total += matriz[a]

if opera��o == 'S':
    print('{:.1f}'.format(total))
else:
    print('{:.1f}'.format(total/len(indices)))
