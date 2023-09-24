n = int(input())
p = []
for i in range(n):
    m= int(input())
    c=0
    p=list(map(int, input().split()))
    p2 = p[:]
    p2.sort(reverse=True)
    for j in range(m):
        if p2[j] == p[j]:
            c +=1
    print(c)