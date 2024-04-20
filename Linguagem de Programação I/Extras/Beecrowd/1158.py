N = int(input())
for _ in range(N):
    X, Y = map(int, input().split())
    if X % 2 == 0:
        X += 1
    soma = 0
    for _ in range(Y):
        soma += X
        X += 2
    print(soma)