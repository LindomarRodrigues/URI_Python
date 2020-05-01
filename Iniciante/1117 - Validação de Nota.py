# -*- coding: utf-8 -*-

notas = []

while True:
    nota = float(input())
    if nota < 0 or nota > 10:
        print('nota invalida')
    else:
        notas.append(nota)
    if len(notas) == 2:
        break
print('media = {:.2f}'.format(sum(notas)/len(notas)))
