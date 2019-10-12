# -*- coding: utf-8 -*-

for a in range(0, 10):
    num = int(input())
    if num <= 0:
        print('X[{}] = 1'.format(a))
    else:
        print('X[{}] = {}'.format(a, num))
