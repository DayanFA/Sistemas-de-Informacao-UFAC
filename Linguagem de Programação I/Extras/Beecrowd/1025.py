import sys
from bisect import bisect_left

T = 1
for line in sys.stdin:
    N, Q = map(int, line.split())
    if N == 0 and Q == 0:
        break

    marmores = sorted(int(sys.stdin.readline()) for _ in range(N))

    print(f'CASE# {T}:')
    T += 1
    for _ in range(Q):
        consulta = int(sys.stdin.readline())
        resposta = bisect_left(marmores, consulta)
        if resposta != len(marmores) and marmores[resposta] == consulta:
            print(f'{consulta} found at {resposta + 1}')
        else:
            print(f'{consulta} not found')