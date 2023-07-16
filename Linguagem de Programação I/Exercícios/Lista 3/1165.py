N = int(input())
for _ in range(N):
    conta = 0
    X = int(input())
    for i in range(1, X+1):
        if X % i == 0:
            conta = conta+1
        else:
            continue
    if conta == 2:
        print('{} eh primo' .format(X))
    else:
        print('{} nao eh primo' .format(X))
