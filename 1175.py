# -*- coding: utf-8 -*-

vetor = []
for a in range(0, 20):
    valor = input()
    vetor.append(valor)

vetor_inv = []
n = 0
for a in range(19, -1, -1):
    print('N[{}] = {}'.format(n, vetor[a]))
    n += 1
