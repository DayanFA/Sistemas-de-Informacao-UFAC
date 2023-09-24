n = int(input())
l = []
for i in range(n):
    c = input()
    v = input()
    l.append((c, v))
d = {}
for t in l:
    if len(t) == 2:
        c, v = t
        d[c] = v
print("Dicionário:", d)


