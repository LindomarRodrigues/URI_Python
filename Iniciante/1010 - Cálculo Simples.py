# -*- coding: utf-8 -*-

pe�a1 = input().split()
pe�a2 = input().split()

quantidade1 = int(pe�a1[1])
valor1 = float(pe�a1[2])

quantidade2 = int(pe�a2[1])
valor2 = float(pe�a2[2])

total = quantidade1*valor1 + quantidade2*valor2

print('VALOR A PAGAR: R$ {:.2f}'.format(total))
