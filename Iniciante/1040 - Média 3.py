# -*- coding: utf-8 -*-

entrada = input().split()
a = float(entrada[0])
b = float(entrada[1])
c = float(entrada[2])
d = float(entrada[3])

media = (a*2 + b*3 + c*4 + d*1)/(2+3+4+1)
print('Media: {:.1f}'.format(media))

if media >= 7:
    print('Aluno aprovado.')
elif media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em exame.')
    nota = float(input())
    print('Nota do exame: {:.1f}'.format(nota))
    media = (nota + media)/2
    if media >= 5:
        print('Aluno aprovado.')
    elif media < 5:
        print('Aluno reprovado.')
    print('Media final: {:.1f}'.format(media))
