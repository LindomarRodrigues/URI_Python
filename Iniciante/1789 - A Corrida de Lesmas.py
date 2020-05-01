# -*- coding: utf-8 -*-

while True:
    try:
        quant = int(input())
        velocidades_str = input().split(' ')

        velocidades = []
        for a in velocidades_str:
            velocidades.append(int(a))

        velocidades = sorted(velocidades, reverse=True)
        veloz = velocidades[0]

        if int(veloz) < 10:
            print(1)
        elif 10 <= int(veloz) < 20:
            print(2)
        elif int(veloz) >= 20:
            print(3)

    except EOFError:
        quit()
