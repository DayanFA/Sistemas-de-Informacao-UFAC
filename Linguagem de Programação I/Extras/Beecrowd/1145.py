m,n = map(int, input().split())
for i in range(1, n+1):
    if i % m == 0:
        print(f'{i}')
    else:
        print(f'{i}', end=' ')