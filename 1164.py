# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    x = int(input())
    divisores = []
    for b in range(1, (x//2)+1):
        if x % b == 0:
            divisores.append(b)
    if sum(divisores) == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))
