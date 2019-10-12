# -*- coding: utf-8 -*-

pares = 0
for a in range(0, 5):
    num = int(input())
    if num % 2 == 0:
        pares += 1
print(pares, 'valores pares')
