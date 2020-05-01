# -*- coding: utf-8 -*-

valor = float(input())
n_100 = 0
n_50 = 0
n_20 = 0
n_10 = 0
n_5 = 0
n_2 = 0

m_1 = 0
m_50 = 0
m_25 = 0
m_10 = 0
m_5 = 0
m_01 = 0


while valor > 0.001:

    if valor >= 100:
        n_100 += 1
        valor -= 100
    elif valor >= 50:
        n_50 += 1
        valor -= 50
    elif valor >= 20:
        n_20 += 1
        valor -= 20
    elif valor >= 10:
        n_10 += 1
        valor -= 10
    elif valor >= 5:
        n_5 += 1
        valor -= 5
    elif valor >= 2:
        n_2 += 1
        valor -= 2
    elif valor >= 1:
        m_1 += 1
        valor -= 1
    elif valor >= 0.5:
        m_50 += 1
        valor -= 0.5
    elif valor >= 0.25:
        m_25 += 1
        valor -= 0.25
    elif valor >= 0.10:
        m_10 += 1
        valor -= 0.10
    elif valor >= 0.05:
        m_5 += 1
        valor -= 0.05
    else:
        m_01 += 1
        valor -= 0.01
print('''NOTAS:
{} nota(s) de R$ 100.00
{} nota(s) de R$ 50.00
{} nota(s) de R$ 20.00
{} nota(s) de R$ 10.00
{} nota(s) de R$ 5.00
{} nota(s) de R$ 2.00'''.format(n_100, n_50, n_20, n_10, n_5, n_2))

print('''MOEDAS:
{} moeda(s) de R$ 1.00
{} moeda(s) de R$ 0.50
{} moeda(s) de R$ 0.25
{} moeda(s) de R$ 0.10
{} moeda(s) de R$ 0.05
{} moeda(s) de R$ 0.01'''.format(m_1, m_50, m_25, m_10, m_5, m_01))
