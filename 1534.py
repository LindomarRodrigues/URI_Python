# -*- coding: utf-8 -*-

while True:
    try:
        n = int(input())
        matriz = []
        for a in range(0, n):
            linha = ''
            for b in range(0, n):
                if a == (n - 1 - b):
                    linha += '2'
                elif a == b:
                    linha += '1'
                else:
                    linha += '3'
            print(linha)
    except:
        break
