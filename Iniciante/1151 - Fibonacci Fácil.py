# -*- coding: utf-8 -*-

sequencia = [0, 1]

n = int(input())
if n == 1:
    print('0')
    quit()
elif n == 2:
    print('0 1')
    quit()

else:
    texto = ''
    while len(sequencia) < n:
        texto = texto + \
            str(int(sequencia[len(sequencia) - 2]) +
                int(sequencia[len(sequencia) - 1])) + ' '
        sequencia.append(
            int(sequencia[len(sequencia)-2])+int(sequencia[len(sequencia)-1]))


print('0 1', texto.strip())
