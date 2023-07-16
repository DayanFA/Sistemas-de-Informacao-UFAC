while True:
    try:
        N = int(input())
        array = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if j == N - 1 - i:  
                    array[i][j] = 2
                elif i == j:  
                    array[i][j] = 1
                else:  
                    array[i][j] = 3

        for i in range(N):
            for j in range(N):
                print(array[i][j], end='')
            print()

    except EOFError:
        break