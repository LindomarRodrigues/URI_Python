# -*- coding: utf-8 -*-

from math import sqrt

entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])

delta = (b**2) - (4*a*c)
if a == 0 or delta < 0:
    print('Impossivel calcular')
    quit()
x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)

print('''R1 = {:.5f}
R2 = {:.5f}'''.format(x1, x2))
