n = int(input())

for i in range(n):
    x, y = [int(a) for a in str(input()).split(' ')]

    resultados = {'Rafael': (3 * x) ** 2 + y ** 2,
                  'Beto': 2 * (x ** 2) + (5 * y) ** 2,
                  'Carlos': -100 * x + y ** 3}
    maior = sorted(resultados.items(), key=lambda kv: (kv[1], kv[0]))[2]
    print('{} ganhou'.format(maior[0]))
