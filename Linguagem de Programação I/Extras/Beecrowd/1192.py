def ca(a):
    n = int(a[0])
    l = a[1]
    nn = int(a[2])
    if n == nn:
        return n * nn
    elif 'A' <= l <= 'Z':
        return nn - n
    else:
        return n + nn
n = int(input())
for _ in range(n):
    l = input()
    r = ca(l)
    print(r)