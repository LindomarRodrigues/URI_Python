# -*- coding: utf-8 -*-

n = int(input())

for a in range(1, n + 1):
    print('{} {} {}'.format(a, a**2, a**3))
    print('{} {} {}'.format(a, (a**2)+1, (a**3)+1))
