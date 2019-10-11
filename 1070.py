# -*- coding: utf-8 -*-

x = int(input())

for a in range(x, x+12, 2):
    if a % 2 != 0:
        print(a)
    else:
        print(a+1)
