# -*- coding: utf-8 -*-

maior = 0
posicao = 0
for a in range(1, 101):
    num = int(input())
    if num > maior:
        maior = num
        posicao = a
print(maior)
print(posicao)
