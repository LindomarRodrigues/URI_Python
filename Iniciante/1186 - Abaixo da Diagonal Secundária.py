# -*- coding: utf-8 -*-

operação = str(input())

indice = [
    23,
    35,  34,
    47,  46,  45,
    59,  58,  57,  56,
    71,  70,  69,  68,  67,
    83,  82,  81,  80,  79,  78,
    95,  94,  93,  92,  91,  90,  89,
    107, 106, 105, 104, 103, 102, 101, 100,
    119, 118, 117, 116, 115, 114, 113, 112, 111,
    131, 130, 129, 128, 127, 126, 125, 124, 123, 122,
    143, 142, 141, 140, 139, 138, 137, 136, 135, 134, 133]

soma = 0
for a in range(0, 144):
    valor = float(input())
    if a in indice:
        soma += valor

if operação == 'S':
    print('{:.1f}'.format(soma))
else:
    print('{:.1f}'.format(soma/len(indice)))
