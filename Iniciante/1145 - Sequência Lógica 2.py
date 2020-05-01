# -*- coding: utf-8 -*-

entrada = input().split()
x = int(entrada[0])
y = int(entrada[1])


for a in range(1, y, x):
    for b in range(a, (a+x)-1):
        print(b, end=' ')
        if b == y:
            quit()
    print((a+x)-1)
