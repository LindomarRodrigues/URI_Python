# -*- coding: utf-8 -*-

from math import factorial
while True:
    try:
        entrada = str(input()).split()
        M = int(entrada[0])
        N = int(entrada[1])

        print(factorial(M)+factorial(N))

    except EOFError:
        quit()
