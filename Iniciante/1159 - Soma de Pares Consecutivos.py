# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0:
        quit()
    total = 0
    if x % 2 == 0:
        for a in range(x, x+10, 2):
            total += a
    else:
        for a in range(x+1, x+11, 2):
            total += a
    print(total)
