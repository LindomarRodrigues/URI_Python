# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, 10):
    if a < 1:
        print('N[0] = {}'.format(n))
        valor = n
    else:
        valor = valor*2
        print('N[{}] = {}'.format(a, valor))
