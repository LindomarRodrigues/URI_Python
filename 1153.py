# -*- coding: utf-8 -*-

n = int(input())

for a in range(n-1, 0, -1):
    n *= a
print(n)
