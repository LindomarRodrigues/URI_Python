# -*- coding: utf-8 -*-

linha = int(input())
operação = str(input())
matriz = []

for a in range(0, 144):
    valor = float(input())
    matriz.append(valor)

if linha == 0:
    inicio = 0
    fim = 11
elif linha == 1:
    inicio = 12
    fim = 23
elif linha == 2:
    inicio = 24
    fim = 35
elif linha == 3:
    inicio = 36
    fim = 47
elif linha == 4:
    inicio = 48
    fim = 59
elif linha == 5:
    inicio = 60
    fim = 71
elif linha == 6:
    inicio = 72
    fim = 83
elif linha == 7:
    inicio = 84
    fim = 95
elif linha == 8:
    inicio = 96
    fim = 107
elif linha == 9:
    inicio = 108
    fim = 119
elif linha == 10:
    inicio = 120
    fim = 131
elif linha == 11:
    inicio = 132
    fim = 143

if operação == 'S':
    resultado = sum(matriz[inicio:fim+1])
elif operação == 'M':
    resultado = sum(matriz[inicio:fim+1])/len(matriz[inicio:fim+1])
print('{:.1f}'.format(resultado))
