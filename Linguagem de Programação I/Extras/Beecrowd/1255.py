n = int(input())
for _ in range(n):
    t = input()
    d = {}
    for i in t:
        if i.isalpha():
            i = i.lower()
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
    m = max(d.values())
    l = []
    for j, f in d.items():
        if f == m:
            l.append(j)
    l.sort()
    print("".join(l))