def ca(p):
    a = 0
    for i in range(1, p + 1):
        n = len(str(i))
        a += n
    return a
p = int(input())
r = ca(p)
print(r)