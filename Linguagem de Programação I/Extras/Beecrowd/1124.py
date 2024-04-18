import math

while True:
    L, C, R1, R2 = map(int, input().split())
    if L == C == R1 == R2 == 0:
        break

    if max(R1, R2) * 2 > min(L, C):
        print('N')
        continue

    if (R1 + R2) ** 2 <= (L - R1 - R2) ** 2 + (C - R1 - R2) ** 2:
        print('S')
    else:
        print('N')