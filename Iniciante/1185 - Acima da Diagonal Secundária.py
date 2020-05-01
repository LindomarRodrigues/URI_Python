# -*- coding: utf-8 -*-

operação = str(input())

total = 0
indice = []
for a in range(10, -1, -1):
    for b in range(a, -1, -1):
        indice.append(b+total)
    total += 12

matriz = []
for a in range(0, 12*12):
    matriz.append(float(input()))

soma = 0
for a in indice:
    soma += matriz[a]

if operação == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(indice)))
