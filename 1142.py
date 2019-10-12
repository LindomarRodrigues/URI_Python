# -*- coding: utf-8 -*-

n = int(input())
linhas = 0
a = 1
b = 2
c = 3

while linhas < n:
    print('{} {} {} PUM'.format(a, b, c))
    a += 4
    b += 4
    c += 4
    linhas += 1
