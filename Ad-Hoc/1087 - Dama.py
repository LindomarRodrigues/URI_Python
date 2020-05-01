# -*- coding: utf-8 -*-

while True:
    entrada = str(input()).split()
    if entrada == ['0', '0', '0', '0']:
        quit()

    x1 = int(entrada[0])
    y1 = int(entrada[1])
    x2 = int(entrada[2])
    y2 = int(entrada[3])

    if x1 == x2 and y1 == y2:
        print(0)

    elif x1 == x2 or y1 == y2:
        print(1)

    elif ((x1 == x2-1) and (y1 == y2 + 1)) or ((x1 == x2-2) and (y1 == y2 + 2)):
        print(1)
    elif ((x1 == x2-3) and (y1 == y2 + 3)) or ((x1 == x2-4) and (y1 == y2 + 4)):
        print(1)
    elif ((x1 == x2-5) and (y1 == y2 + 5)) or ((x1 == x2-6) and (y1 == y2 + 6)):
        print(1)
    elif ((x1 == x2-7) and (y1 == y2 + 7)) or ((x1 == x2-8) and (y1 == y2 + 8)):
        print(1)

    elif ((x1 == x2+1) and (y1 == y2 - 1)) or ((x1 == x2+2) and (y1 == y2 - 2)):
        print(1)
    elif ((x1 == x2+3) and (y1 == y2 - 3)) or ((x1 == x2+4) and (y1 == y2 - 4)):
        print(1)
    elif ((x1 == x2+5) and (y1 == y2 - 5)) or ((x1 == x2+6) and (y1 == y2 - 6)):
        print(1)
    elif ((x1 == x2+7) and (y1 == y2 - 7)) or ((x1 == x2+8) and (y1 == y2 - 8)):
        print(1)

    elif ((x1 == x2+1) and (y1 == y2 + 1)) or ((x1 == x2+2) and (y1 == y2 + 2)):
        print(1)
    elif ((x1 == x2+3) and (y1 == y2 + 3)) or ((x1 == x2+4) and (y1 == y2 + 4)):
        print(1)
    elif ((x1 == x2+5) and (y1 == y2 + 5)) or ((x1 == x2+6) and (y1 == y2 + 6)):
        print(1)
    elif ((x1 == x2+7) and (y1 == y2 + 7)) or ((x1 == x2+8) and (y1 == y2 + 8)):
        print(1)

    elif ((x1 == x2-1) and (y1 == y2 - 1)) or ((x1 == x2-2) and (y1 == y2 - 2)):
        print(1)
    elif ((x1 == x2-3) and (y1 == y2 - 3)) or ((x1 == x2-4) and (y1 == y2 - 4)):
        print(1)
    elif ((x1 == x2-5) and (y1 == y2 - 5)) or ((x1 == x2-6) and (y1 == y2 - 6)):
        print(1)
    elif ((x1 == x2-7) and (y1 == y2 - 7)) or ((x1 == x2-8) and (y1 == y2 - 8)):
        print(1)

    else:
        print(2)
