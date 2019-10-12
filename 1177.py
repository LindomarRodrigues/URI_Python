# -*- coding: utf-8 -*-

t = int(input())
h = 0
for b in range(0, 1000):
    if h > 999:
        break
    for a in range(0, t):
        print('N[{}] = {}'.format(h, a))
        h += 1
        if h > 999:
            break
