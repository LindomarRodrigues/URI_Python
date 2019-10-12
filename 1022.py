# -*- coding: utf-8 -*-

from fractions import Fraction
n = int(input())

for a in range(n):
    entrada = str(input()).split(' ')
    if entrada[3] == '+':
        numerador = int(
            float(entrada[0]) * float(entrada[6]) + float(entrada[4]) * float(entrada[2]))
        divisor = int(float(entrada[2]) * float(entrada[6]))
        if divisor < 0:
            numerador = int('-'+str(numerador))
            divisor = abs(divisor)
        simplificado = Fraction(numerador, divisor)

    elif entrada[3] == '-':
        numerador = int(
            float(entrada[0]) * float(entrada[6]) - float(entrada[4]) * float(entrada[2]))
        divisor = int(float(entrada[2]) * float(entrada[6]))
        if divisor < 0:
            numerador = int('-'+str(numerador))
            divisor = abs(divisor)
        simplificado = Fraction(numerador, divisor)

    elif entrada[3] == '*':
        numerador = int(float(entrada[0]) * float(entrada[4]))
        divisor = int(float(entrada[2]) * float(entrada[6]))
        if divisor < 0:
            numerador = int('-'+str(numerador))
            divisor = abs(divisor)
        simplificado = Fraction(numerador, divisor)

    elif entrada[3] == '/':
        numerador = int(float(entrada[0]) * float(entrada[6]))
        divisor = int(float(entrada[4]) * float(entrada[2]))
        if divisor < 0:
            numerador = int('-'+str(numerador))
            divisor = abs(divisor)
        simplificado = Fraction(numerador, divisor)

    print('{}/{} = {}/{}'.format(numerador, divisor,
                                 simplificado.numerator, simplificado.denominator))
