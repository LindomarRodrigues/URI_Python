# -*- coding: utf-8 -*-

n = int(input())

for a in range(1, (n//2)+1):
    if n % a == 0:
        print(a)
print(n)
