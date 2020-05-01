# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    valores = list(map(float, input().split()))
    if valores[1] == 0:
        print('divisao impossivel')
    else:
        print('{:.1f}'.format(valores[0]/valores[1]))
