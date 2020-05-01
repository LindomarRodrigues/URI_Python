# -*- coding: utf-8 -*-

coluna = int(input())
operação = input()

valores = []
valor = 0
for a in range(0, 144):
    valor = float(input())
    valores.append(valor)


v_coluna = []
for a in range(coluna, 144, 12):
    v_coluna.append(valores[a])

if operação == 'S':
    print('{:.1f}'.format(sum(v_coluna)))
elif operação == 'M':
    print('{:.1f}'.format(sum(v_coluna)/12))
