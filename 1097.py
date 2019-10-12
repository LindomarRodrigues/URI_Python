# -*- coding: utf-8 -*-

n = 7

for a in range(1, 10, 2):
    print('I={} J={}'.format(a, n))
    n -= 1
    print('I={} J={}'.format(a, n))
    n -= 1
    print('I={} J={}'.format(a, n))
    n += 4
