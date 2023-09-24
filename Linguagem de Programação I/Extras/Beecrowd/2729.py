n = int(input())
for _ in range(n):
    l = input().split()
    l = sorted(set(l))
    print(' '.join(l))