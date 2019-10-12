# -*- coding: utf-8 -*-

n = int(input())
for a in range(1, n+1):
    if a % 2 == 0:
        print('{}^2 = {}'.format(a, a**2))
