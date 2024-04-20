while True:
    N = int(input().strip())
    if N == 0:
        break

    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = 2 ** (i + j)

    width = len(str(matrix[N-1][N-1]))
    for i in range(N):
        for j in range(N):
            if j == N - 1:
                print("{:>{}}".format(matrix[i][j], width))
            else:
                print("{:>{}}".format(matrix[i][j], width), end=" ")
    print()