N = int(input())
for _ in range(N):
    R = 0
    X = int(input())
    for i in range(1, X):
        if X % i == 0:
            R += i
    if R == X:
        print('{} eh perfeito'.format(X))
    else:
        print('{} nao eh perfeito' .format(X))