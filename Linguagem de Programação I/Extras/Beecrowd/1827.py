import sys

for line in sys.stdin:
    N = int(line.strip())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                matrix[i][j] = 2
            if i + j == N - 1:
                matrix[i][j] = 3
            if N // 3 <= i < N - N // 3 and N // 3 <= j < N - N // 3:
                matrix[i][j] = 1
            if i == j and i == N // 2:
                matrix[i][j] = 4
    for row in matrix:
        print("".join(map(str, row)))
    print()