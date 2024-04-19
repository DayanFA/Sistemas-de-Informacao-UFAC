t = int(input())
for _ in range(t):
    n = list(input().strip())
    n.sort()
    if n[0] == '0':
        for i in range(1, len(n)):
            if n[i] != '0':
                n[0], n[i] = n[i], n[0]
                break
    print(''.join(n))