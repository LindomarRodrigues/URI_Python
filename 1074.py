# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    num = int(input())
    if num == 0:
        print('NULL')
    elif num > 0 and num % 2 == 0:
        print('EVEN POSITIVE')
    elif num < 0 and num % 2 == 0:
        print('EVEN NEGATIVE')
    elif num > 0 and num % 2 != 0:
        print('ODD POSITIVE')
    elif num < 0 and num % 2 != 0:
        print('ODD NEGATIVE')
