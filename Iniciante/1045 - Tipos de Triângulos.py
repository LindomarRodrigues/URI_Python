# -*- coding: utf-8 -*-

entrada = input().split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])
entrada.clear()
entrada.append(A)
entrada.append(B)
entrada.append(C)
entrada.sort()
a = entrada[2]
b = entrada[1]
c = entrada[0]

if a >= b+c:
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == b**2 + c**2:
        print('TRIANGULO RETANGULO')
    if a**2 > b**2 + c**2:
        print('TRIANGULO OBTUSANGULO')
    if a**2 < b**2 + c**2:
        print('TRIANGULO ACUTANGULO')
    if a == b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or a == c or b == c:
        print('TRIANGULO ISOSCELES')
