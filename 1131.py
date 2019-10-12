# -*- coding: utf-8 -*-

questão = 1
total = 0
vit_inter = 0
vit_gremio = 0
empates = 0

while True:
    resultado = str(input()).split()
    gols_inter = int(resultado[0])
    gols_gremio = int(resultado[1])
    total += 1

    if gols_inter > gols_gremio:
        vit_inter += 1
    elif gols_inter < gols_gremio:
        vit_gremio += 1
    elif gols_inter == gols_gremio:
        empates += 1
    questão = int(input("Novo grenal (1-sim 2-nao)\n"))
    if questão == 2:
        break

if vit_inter > vit_gremio:
    frase = 'Inter venceu mais'
elif vit_inter < vit_gremio:
    frase = 'Gremio venceu mais'
elif vit_inter == vit_gremio:
    frase = 'Nao houve vencedor'

print('''{} grenais
Inter:{}
Gremio:{}
Empates:{}
{}'''.format(total, vit_inter, vit_gremio, empates, frase))
