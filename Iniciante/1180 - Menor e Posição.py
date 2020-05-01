# -*- coding: utf-8 -*-

n = int(input())
vetor = input().split()

for a in range(0, n):
    valor = int(vetor[a])
    if a == 0:
        menor = valor
        pos = a
    elif a > 0:
        if valor < menor:
            menor = valor
            pos = a
print('Menor valor: {}'.format(menor))
print('Posicao: {}'.format(pos))
