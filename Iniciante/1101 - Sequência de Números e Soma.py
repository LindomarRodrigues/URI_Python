# -*- coding: utf-8 -*-

m = 1
n = 1
soma = 0
sequencia = ''
while True:
    entrada = list(map(int, (input().split(' '))))
    if entrada[0] <= 0 or entrada[1] <= 0:
        break
    entrada.sort()
    sequencia = ''
    soma = 0
    for a in range(entrada[0], entrada[1]+1):
        sequencia = (sequencia + ' ' + str(a)).strip()
        soma += a
    print(sequencia, 'Sum='+str(soma))
