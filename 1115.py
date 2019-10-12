# -*- coding: utf-8 -*-

x = 1
y = 1
while True:
    entrada = list(map(int, input().split()))
    x = entrada[0]
    y = entrada[1]
    if x == 0 or y == 0:
        break
    if x > 0 and y > 0:
        print('primeiro')
    elif x < 0 and y > 0:
        print('segundo')
    elif x < 0 and y < 0:
        print('terceiro')
    elif x > 0 and y < 0:
        print('quarto')
