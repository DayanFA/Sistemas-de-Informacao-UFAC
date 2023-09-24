n = int(input())
for _ in range(n):
    m = int(input())
    p = {}
    for _ in range(m):
        f, s = input().strip().split(' ')
        p[f] = float(s)
    P = int(input())
    r = 0.0
    for _ in range(P):
        f, q = input().strip().split(' ')
        r += int(q) * p[f]
    print("R$ {:.2f}".format(r))