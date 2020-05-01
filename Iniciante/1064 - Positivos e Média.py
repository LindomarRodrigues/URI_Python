# -*- coding: utf-8 -*-

soma = 0
positivos = 0
for a in range(0, 6):
    num = float(input())
    if num > 0:
        positivos += 1
        soma += num
print('{} valores positivos'.format(positivos))
media = soma/positivos
print('{:.1f}'.format(media))
