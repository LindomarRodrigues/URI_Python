# -*- coding: utf-8 -*-

entrada = str(input()).split()
A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

triangulo = (A * C)/2
circulo = 3.14159 * C**2
trapezio = ((A + B) * C)/2
quadrado = B**2
retangulo = A * B
print('''TRIANGULO: {:.3f}
CIRCULO: {:.3f}
TRAPEZIO: {:.3f}
QUADRADO: {:.3f}
RETANGULO: {:.3f}'''.format(triangulo, circulo, trapezio, quadrado, retangulo))
