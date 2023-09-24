def ca(n):
    c = 0
    while n > 0:
        if n % 2 == 1:
            c += 1
        n = n // 2
    return c
n = int(input())
for _ in range(n):
    a = int(input())
    r = ca(a)
    print(r)