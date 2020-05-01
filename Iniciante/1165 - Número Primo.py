# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    valor = int(input())
    primo = 0
    for b in range(2, valor):
        if valor % b == 0:
            print('{} nao eh primo'.format(valor))
            primo = 1
            break
    if primo == 0:
        print('{} eh primo'.format(valor))
