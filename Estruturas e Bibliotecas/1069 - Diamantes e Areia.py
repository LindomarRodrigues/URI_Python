# -*- coding: utf-8 -*-


def solucionar(linha):
    linha = linha.replace('.', '')
    diamantes = 0
    while linha.count('<>') != 0:
        diamantes += linha.count('<>')
        linha = linha.replace('<>', '')
    return diamantes


n = int(input())

for a in range(n):
    linha = input()
    print(solucionar(linha))
