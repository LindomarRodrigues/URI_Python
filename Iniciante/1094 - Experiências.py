# -*- coding: utf-8 -*-

n = int(input())
Total = 0
Total_de_coelhos = 0
Total_de_ratos = 0
Total_de_sapos = 0

for a in range(0, n):
    base = input().split(' ')
    Total += int(base[0])
    if base[1] == 'C':
        Total_de_coelhos += int(base[0])
    elif base[1] == 'R':
        Total_de_ratos += int(base[0])
    elif base[1] == 'S':
        Total_de_sapos += int(base[0])

Percentual_de_coelhos = (Total_de_coelhos/Total)*100
Percentual_de_ratos = (Total_de_ratos/Total)*100
Percentual_de_sapos = (Total_de_sapos/Total)*100

print('''Total: {} cobaias
Total de coelhos: {}
Total de ratos: {}
Total de sapos: {}'''.format(Total, Total_de_coelhos, Total_de_ratos, Total_de_sapos))
print('''Percentual de coelhos: {:.2f} %
Percentual de ratos: {:.2f} %
Percentual de sapos: {:.2f} %'''.format(Percentual_de_coelhos, Percentual_de_ratos, Percentual_de_sapos))
