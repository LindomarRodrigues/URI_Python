# -*- coding: utf-8 -*-

inicial = float(input())

valor = inicial
for a in range(0, 100):
    print('N[{}] = {:.4f}'.format(a, valor))
    valor /= 2
