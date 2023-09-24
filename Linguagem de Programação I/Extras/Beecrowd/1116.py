N = int(input())

for i in range(N):
    x,y = map(float, input().split())
    if y == 0:
        print('divisao impossivel')
    else:
        r = x/y
        print('{:.1f}' .format(r))