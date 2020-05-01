# -*- coding: utf-8 -*-

linha = ''

while True:
    N = int(input())

    if N != 0:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                for item in range(1, (N + 1)//2 + 1):
                    if i == item or j == item or i == N + 1 - item or j == N + 1 - item:
                        if item < 10:
                            linha += '  {}'.format(item)
                        else:
                            linha += ' {}'.format(item)
                        if j != N:
                            linha += ' '
                        break
            print(linha)
            linha = ''
    else:
        quit()
    print()
