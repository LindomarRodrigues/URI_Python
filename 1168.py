# -*- coding: utf-8 -*-

n = int(input())

for a in range(0, n):
    num = str(input())
    total = 0

    for b in range(0, len(num)):
        if int(num[b]) == 0:
            total += 6
        elif int(num[b]) == 1:
            total += 2
        elif int(num[b]) == 2:
            total += 5
        elif int(num[b]) == 3:
            total += 5
        elif int(num[b]) == 4:
            total += 4
        elif int(num[b]) == 5:
            total += 5
        elif int(num[b]) == 6:
            total += 6
        elif int(num[b]) == 7:
            total += 3
        elif int(num[b]) == 8:
            total += 7
        elif int(num[b]) == 9:
            total += 6
    print(total, 'leds')
