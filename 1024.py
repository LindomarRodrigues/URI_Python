# -*- coding: utf-8 -*-


def encriptador(linha):
    linha_new = ''

    for letra in linha:
        if letra.isalpha():
            letra_new = chr(ord(letra) + 3)
            linha_new += letra_new
        else:
            linha_new += letra

    linha_new = linha_new[::-1]

    linha_final = linha_new[:len(linha_new)//2]
    for a in range(len(linha_new)//2, len(linha_new)):
        letra_new = chr(ord(linha_new[a]) - 1)
        linha_final += letra_new

    return linha_final


n = int(input())


for a in range(n):
    linha = str(input())
    encri = encriptador(linha)
    print(encri)
