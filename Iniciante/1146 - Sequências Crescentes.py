# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0:
        quit()
    for a in range(1, x):
        print(a, end=' ')
    print(x)
