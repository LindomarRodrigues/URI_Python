# -*- coding: utf-8 -*-

x = int(input())
while True:
    z = int(input())
    if z > x:
        break

quantidade = 0
valor = x
soma = 0
while True:
    soma += valor
    valor += 1
    quantidade += 1
    if soma > z:
        print(quantidade)
        break
