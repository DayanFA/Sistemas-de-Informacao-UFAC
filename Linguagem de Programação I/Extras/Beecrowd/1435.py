while True:
    N = int(input().strip())
    if N == 0:
        break

    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(i, j, N - i - 1, N - j - 1) + 1

    for i in range(N):
        for j in range(N):
            if j == N - 1:
                print("{:3d}".format(matrix[i][j]))
            else:
                print("{:3d}".format(matrix[i][j]), end=" ")
    print()