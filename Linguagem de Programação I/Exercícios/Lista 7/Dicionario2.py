n = int(input())
d = {}
for _ in range(n):
    c = input()
    v = input()
    d[c] = v
l = sorted(d.items())
print("Lista de tuplas:", l)

