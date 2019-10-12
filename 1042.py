# -*- coding: utf-8 -*-

entrada = input().split()
a = int(entrada[0])
b = int(entrada[1])
c = int(entrada[2])

crescente = [a, b, c]
crescente.sort()

print('''{}
{}
{}

{}
{}
{}'''.format(crescente[0], crescente[1], crescente[2], a, b, c))
