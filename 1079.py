# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    entrada = input().split()
    a = float(entrada[0])
    b = float(entrada[1])
    c = float(entrada[2])

    media = (a*2 + b*3 + c*5)/(2+3+5)
    print('{:.1f}'.format(media))
