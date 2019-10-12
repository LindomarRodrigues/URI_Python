# -*- coding: utf-8 -*-

i = 0
while i <= 2:
    if i in [0, 1, 2]:
        print('I={} J={}'.format(int(i), int(i + 1)))
        print('I={} J={}'.format(int(i), int(i + 2)))
        print('I={} J={}'.format(int(i), int(i + 3)))
    else:
        print('I={} J={}'.format(i, i+1))
        print('I={} J={}'.format(i, i + 2))
        print('I={} J={}'.format(i, i + 3))
    i += 0.2
    i = float('{:.1f}'.format(i))
