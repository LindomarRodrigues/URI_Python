# -*- coding: utf-8 -*-

coluna = int(input())
opera��o = input()

valores = []
valor = 0
for a in range(0, 144):
    valor = float(input())
    valores.append(valor)


v_coluna = []
for a in range(coluna, 144, 12):
    v_coluna.append(valores[a])

if opera��o == 'S':
    print('{:.1f}'.format(sum(v_coluna)))
elif opera��o == 'M':
    print('{:.1f}'.format(sum(v_coluna)/12))
