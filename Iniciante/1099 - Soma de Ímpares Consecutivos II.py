# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    entrada = list(map(int, input().split()))
    entrada.sort()
    soma = 0
    for b in range(entrada[0]+1, entrada[1]):
        if b % 2 != 0:
            soma += b
    print(soma)
