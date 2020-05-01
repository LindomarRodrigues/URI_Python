# -*- coding: utf-8 -*-

n = int(input())

lista = []
for i in range(n):
    valor = int(input())
    lista.append(valor)

lista.sort()
new_lista = []
for num in lista:
    if num not in new_lista:
        new_lista.append(num)
        print("{} aparece {} vez(es)".format(num, lista.count(num)))
