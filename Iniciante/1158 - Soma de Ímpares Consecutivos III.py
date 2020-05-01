# -*- coding: utf-8 -*-

n = int(input())
for a in range(0, n):
    valor = str(input()).split()
    x = int(valor[0])
    y = int(valor[1])
    total = 0
    if x % 2 != 0:
        for b in range(x, x+(y*2), 2):
            total += b
    else:
        for b in range(x+1, x+1+(y*2), 2):
            total += b
    print(total)
