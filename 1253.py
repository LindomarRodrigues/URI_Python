# -*- coding: utf-8 -*-

alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input())

for a in range(n):
    frase = str(input())
    indice = int(input())
    frase_deco = ''
    for letra in frase:
        frase_deco += alfabeto[alfabeto.index(letra)-indice]
    print(frase_deco)
