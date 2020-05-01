# -*- coding: utf-8 -*-

while True:
    try:
        entrada = str(input()).split()
        x = int(entrada[0])
        y = int(entrada[1])
        print(x ^ y)
    except EOFError:
        quit()
