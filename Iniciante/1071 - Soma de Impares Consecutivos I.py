# -*- coding: utf-8 -*-

a = int(input())
b = int(input())

soma = 0

if a < b:
    for i in range(a+1, b):
        if i % 2 != 0:
            soma += i
if a == b:
    soma = 0
if a > b:
    for i in range(b+1, a):
        if i % 2 != 0:
            soma += i

print(soma)
