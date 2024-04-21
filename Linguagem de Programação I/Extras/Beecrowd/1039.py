import math

while True:
    try:
        R1, X1, Y1, R2, X2, Y2 = map(int, input().split())
        distance = math.sqrt((X2 - X1) ** 2 + (Y2 - Y1) ** 2)
        if R1 >= distance + R2:
            print('RICO')
        else:
            print('MORTO')
    except EOFError:
        break