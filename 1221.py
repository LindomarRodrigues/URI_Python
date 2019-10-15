# -*- coding: utf-8 -*-
import math


def solucionar(valor):
    if valor == 2:
        return 'Prime'
    elif valor % 2 == 0:
        return 'Not Prime'
    else:
        for temp in range(3, int(math.sqrt(valor)) + 1, 2):
            if valor % temp == 0:
                return 'Not Prime'
    return 'Prime'


n = int(input())

for i in range(n):
    valor = int(input())
    print(solucionar(valor))
