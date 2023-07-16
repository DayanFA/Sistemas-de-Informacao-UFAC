N = int(input())
for _ in range(N):
    x1,x2,x3 = map(float, input().split())
    R = x1*2 + x2*3 + x3*5
    R= R/10.0
    print('{:.1f}'.format(R))