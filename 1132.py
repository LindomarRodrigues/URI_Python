# -*- coding: utf-8 -*-

a = int(input())
b = int(input())

valores = list(map(int, (a, b)))
valores.sort()
soma = 0
for a in range(valores[0], valores[1]+1):
    if a % 13 != 0:
        soma += a
print(soma)
