# -*- coding: utf-8 -*-

while int(input()) != 0:
    entrada = input().split()
    maria = 0
    joao = 0
    for a in entrada:
        if a == '0':
            maria += 1
        elif a == '1':
            joao += 1
    print('Mary won {} times and John won {} times'.format(maria, joao))
