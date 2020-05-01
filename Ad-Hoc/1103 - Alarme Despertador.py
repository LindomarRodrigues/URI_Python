# -*- coding: utf-8 -*-

while True:
    entrada = input()
    if entrada == '0 0 0 0':
        quit()
    entrada = entrada.split()
    if entrada == ['0', '0', '0', '0']:
        quit()
    inicial = int(entrada[0])*60 + int(entrada[1])
    final = int(entrada[2])*60 + int(entrada[3])
    if final > inicial:
        print(final - inicial)
    elif final < inicial:
        print(final-inicial+(60*24))
    else:
        print(24*60)
