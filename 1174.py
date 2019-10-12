# -*- coding: utf-8 -*-

pos = []
valores = []
for a in range(0, 100):
    valor = float(input())
    if valor <= 10:
        valores.append(valor)
        pos.append(a)
for a in range(0, len(pos)):
    print('A[{}] = {}'.format(pos[a], valores[a]))
