n = int(input())
for _ in range(n):
    a, b = input().split()
    c= ""
    m = min(len(a), len(b))
    for i in range(m):
        c += a[i] + b[i]
    c += a[m:] + b[m:]
    print(c)