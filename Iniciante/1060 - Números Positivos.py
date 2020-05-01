# -*- coding: utf-8 -*-

positivos = 0

for a in range(0, 6):
    valor = float(input())
    if valor > 0:
        positivos += 1

print('{} valores positivos'.format(positivos))
