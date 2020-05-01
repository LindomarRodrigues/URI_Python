# -*- coding: utf-8 -*-

for n in range(int(input())):
    quant = float(input())
    dias = 0
    while quant > 1:
        quant /= 2
        dias += 1

    print(dias, 'dias')
