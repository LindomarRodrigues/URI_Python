# -*- coding: utf-8 -*-

num = int(input())
horas = int(input())
por_hora = float(input())

sálario = horas * por_hora

print('NUMBER = {}\n'
      'SALARY = U$ {:.2f}'.format(num, sálario))
