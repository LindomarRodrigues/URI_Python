# -*- coding: utf-8 -*-

entrada = input().split()
inicio = int(entrada[0])
final = int(entrada[1])

if inicio > final:
    duracao = 24-inicio+final
elif inicio == final:
    duracao = 24
elif inicio < final:
    duracao = final-inicio

print('O JOGO DUROU {} HORA(S)'.format(duracao))
