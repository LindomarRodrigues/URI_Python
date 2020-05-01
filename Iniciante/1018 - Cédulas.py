# -*- coding: utf-8 -*-

valor = int(input())

cem = valor//100
cinquenta = (valor-(cem*100))//50
vinte = (valor-(cem*100+cinquenta*50))//20
dez = (valor-(cem*100+cinquenta*50+vinte*20))//10
cinco = (valor-(cem*100+cinquenta*50+vinte*20+dez*10))//5
dois = (valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5))//2
um = (valor-(cem*100+cinquenta*50+vinte*20+dez*10+cinco*5+dois*2))
print('{}\n'
      '{} nota(s) de R$ 100,00\n'
      '{} nota(s) de R$ 50,00\n'
      '{} nota(s) de R$ 20,00\n'
      '{} nota(s) de R$ 10,00\n'
      '{} nota(s) de R$ 5,00\n'
      '{} nota(s) de R$ 2,00\n'
      '{} nota(s) de R$ 1,00'.format(valor, cem, cinquenta, vinte, dez, cinco, dois, um))
