# -*- coding: utf-8 -*-

x = 0
while x != 2:
    total = 0
    valor = 0
    while total < 2:
        x = float(input())
        if 0 <= x <= 10 and x != 2:
            valor += x
            total += 1
        else:
            print('nota invalida')
    print('''media = {:.2f}'''.format(valor/2))

    resposta = 0
    while resposta not in [1, 2]:
        print('novo calculo (1-sim 2-nao)')
        resposta = float(input())
        if resposta == 2:
            quit()
