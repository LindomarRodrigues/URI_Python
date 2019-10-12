# -*- coding: utf-8 -*-

operação = str(input())

matriz = []
for a in range(0, 12 * 12):
    matriz.append(float(input()))

indices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           14, 15, 16, 17, 18, 19, 20, 21,
           27, 28, 29, 30, 31, 32,
           40, 41, 42, 43,
           53, 54]
soma = 0
for a in indices:
    soma += matriz[a]
if operação == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(indices)))
