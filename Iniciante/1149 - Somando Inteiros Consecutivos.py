# -*- coding: utf-8 -*-

entrada = str(input()).split()
A = int(entrada[0])
valor = 0
for a in range(1, len(entrada)):
    if int(entrada[a]) > 0:
        for b in range(0, int(entrada[a])):
            valor += A+b
print(valor)
