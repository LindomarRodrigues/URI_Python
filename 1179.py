# -*- coding: utf-8 -*-

impar = []
par = []
for a in range(0, 15):
    n = int(input())
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if len(par) == 5:
        for b in range(0, 5):
            print('par[{}] = {}'.format(b, par[b]))
        par = []
    if len(impar) == 5:
        for b in range(0, 5):
            print('impar[{}] = {}'.format(b, impar[b]))
        impar = []

for b in range(0, len(impar)):
    print('impar[{}] = {}'.format(b, impar[b]))
for b in range(0, len(par)):
    print('par[{}] = {}'.format(b, par[b]))
