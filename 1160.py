# -*- coding: utf-8 -*-

for a in range(0, int(input())):
    entrada = str(input()).split()
    qa = float(entrada[0])
    qb = float(entrada[1])
    ca = float(entrada[2])/100
    cb = float(entrada[3])/100
    anos = 0
    while True:
        qa += int(qa*ca)
        qb += int(qb*cb)
        anos += 1
        if qa > qb:
            print('{} anos.'.format(anos))
            break
        if anos == 100:
            print('Mais de 1 seculo.')
            break
