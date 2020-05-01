# -*- coding: utf-8 -*-

operação = str(input())

indice = [







    89,  90,
    100, 101, 102, 103,
    111, 112, 113, 114, 115, 116,
    122, 123, 124, 125, 126, 127, 128, 129,
    133, 134, 135, 136, 137, 138, 139, 140, 141, 142, ]

soma = 0
for a in range(0, 144):
    valor = float(input())
    if a in indice:
        soma += valor

if operação == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(indice)))
