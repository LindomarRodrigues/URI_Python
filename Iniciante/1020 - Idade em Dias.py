# -*- coding: utf-8 -*-

dias_total = int(input())
anos = dias_total//365
meses = (dias_total-(anos*365))//30
dias = dias_total-((anos*365)+meses*30)

print('{} ano(s)'.format(anos))
print('{} mes(es)'.format(meses))
print('{} dia(s)'.format(dias))
