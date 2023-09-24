n = int(input())

for _ in range(n):
    v= input()
    h=''
    k = len(v) // 2
    for i in range (k):
        g1=v[:k]
        e1 = g1[::-1]
        g2 = v[k:]
        e2 = g2[::-1]
        h=e1 + e2
    print(h)