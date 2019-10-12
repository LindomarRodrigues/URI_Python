# -*- coding: utf-8 -*-

S = 0
denominador = 1
for a in range(1, 40, 2):
    S += a/denominador
    denominador *= 2
print('{:.2f}'.format(S))
