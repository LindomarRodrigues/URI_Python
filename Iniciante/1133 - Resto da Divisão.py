# -*- coding: utf-8 -*-

valores = sorted([int(input()), int(input())])

for a in range(valores[0] + 1, valores[1]):
    resto = a % 5
    if resto in [2, 3]:
        print(a)
