def r(x, y):
    return (3 * x) ** 2 + y ** 2
def b(x, y):
    return 2 * (x ** 2) + (5 * y) ** 2
def c(x, y):
    return -100 * x + y ** 3
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    raf = r(x, y)
    bet = b(x, y)
    car = c(x, y)
    if raf > bet and raf > car:
        print('Rafael ganhou')
    elif bet > raf and bet > car:
        print('Beto ganhou')
    else:
        print('Carlos ganhou')