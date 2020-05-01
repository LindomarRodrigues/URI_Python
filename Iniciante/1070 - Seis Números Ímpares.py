# -*- coding: utf-8 -*-

x = int(input())
if x % 2 != 0:
    for a in range(x, x+12, 2):
        print(a)
elif x % 2 == 0:
    for a in range(x+1, x+13, 2):
        print(a)
