# -*- coding: utf-8 -*-

soma = 0
total = 0
while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        soma += idade
        total += 1
print('{:.2f}'.format(soma/total))
