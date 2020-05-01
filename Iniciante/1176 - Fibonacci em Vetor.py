# -*- coding: utf-8 -*-

t = int(input())

fib = [0, 0, 1]
for a in range(0, t):
    n = int(input())
    while len(fib) < n+2:
        fib.append(fib[-1]+fib[-2])
    print('Fib({}) = {}'.format(n, fib[n+1]))
