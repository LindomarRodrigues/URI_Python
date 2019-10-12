# -*- coding: utf-8 -*-

salario = float(input())
imposto = 0

if salario < 2000:
    print('Isento')
    quit()

elif 2000 < salario <= 3000:
    salario = salario-2000
    imposto = salario*(8/100)

elif 3000 < salario <= 4500:
    salario = salario-3000
    imposto1 = 1000 * (8/100)
    imposto2 = salario*(18/100)
    imposto = imposto1 + imposto2

elif salario > 4500:
    salario = salario-4500
    imposto1 = 1000 * (8 / 100)
    imposto2 = 1500 * (18 / 100)
    imposto3 = salario*(28/100)
    imposto = imposto1 + imposto2 + imposto3

print('R$ {:.2f}'.format(imposto))
