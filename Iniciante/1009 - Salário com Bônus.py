# -*- coding: utf-8 -*-

nome = input()
fixo = float(input())
vendas = float(input())

sálario = fixo + (vendas * (15/100))

print('TOTAL = R$ {:.2f}'.format(sálario))
