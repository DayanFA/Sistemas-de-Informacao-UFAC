import sys
import math

T = 0
for line in sys.stdin:
    N = int(line)
    if N == 0:
        break

    if T:
        print('')

    totalX, totalY = 0, 0
    consumos = {}
    for _ in range(N):
        X, Y = map(int, sys.stdin.readline().split())
        totalX += X
        totalY += Y
        consumos[Y // X] = consumos.get(Y // X, 0) + X

    T += 1
    print(f'Cidade# {T}:')

    output = []
    keys = sorted(consumos.keys())
    for key in keys:
        output.append(f'{consumos[key]}-{key}')

    print(' '.join(output))

    consumo_medio = math.floor((100 * totalY) / totalX) / 100
    print(f'Consumo medio: {consumo_medio:.2f} m3.')