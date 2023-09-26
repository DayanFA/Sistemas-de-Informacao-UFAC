n, cap = map(int, input().split())
c = 0
ee = False
for _ in range(n):
    s, e = map(int, input().split())
    c -= s
    c += e
    if c > cap:
        ee = True
if ee:
    print('S')
else:
    print('N')
