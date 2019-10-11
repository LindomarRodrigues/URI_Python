# -*- coding: utf-8 -*-

peça1 = input().split()
peça2 = input().split()

quantidade1 = int(peça1[1])
valor1 = float(peça1[2])

quantidade2 = int(peça2[1])
valor2 = float(peça2[2])

total = quantidade1*valor1 + quantidade2*valor2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
