# -*- coding: utf-8 -*-

for a in range(int(input())):
    entrada = input().split(' ')

    string1 = entrada[0]
    string2 = entrada[1]

    resultado = ''

    if len(string1) > len(string2):
        maior = len(string1)
    else:
        maior = len(string2)

    for a in range(0, maior):
        try:
            resultado += string1[a]
        except:
            None

        try:
            resultado += string2[a]
        except:
            None
    print(resultado)
