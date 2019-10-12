# -*- coding: utf-8 -*-

salario = float(input())

if 0 <= salario <= 400:
    percentual = 15
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
elif 400.01 <= salario <= 800:
    percentual = 12
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
if 800.01 <= salario <= 1200:
    percentual = 10
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
if 1200.01 < salario <= 2000:
    percentual = 7
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste
if salario > 2000:
    percentual = 4
    reajuste = salario * (percentual / 100)
    novo_salario = salario + reajuste

print('Novo salario: {:.2f}'.format(novo_salario))
print('Reajuste ganho: {:.2f}'.format(reajuste))
print('Em percentual: {} %'.format(percentual))
