n, t = map(int, input().split())
v = []
for i in range(n):
    jo, ni = input().split()
    v.append((-int(ni), jo))
v.sort()
for i in range(1, t + 1):
    print("Time", i)
    ti = []
    for k in range(i - 1, n, t):
        ti.append(v[k][1])
    for j in sorted(ti):
        print(j)
    print()