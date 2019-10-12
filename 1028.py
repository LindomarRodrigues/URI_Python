# -*- coding: utf-8 -*-


def mdc(x, y):
    while y:
        x, y = y, x % y

    return x


for n in range(int(input())):
    entrada = input().split(' ')
    a = int(entrada[0])
    b = int(entrada[1])
    print(mdc(a, b))
