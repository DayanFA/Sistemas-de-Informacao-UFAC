n = int(input())
while n != 0:
    c = 0
    d = {}
    for i in range(n):
        w1, w2 = input().split()
        d[w1] = w2
    m = int(input())
    for i in range(m):
        w1, w2 = input().split()
        cc = 0
        o = d[w1]
        for j in range(len(w2)):
            if o[j] != w2[j]:
                cc += 1
                if cc > 1:
                    c += 1
                    break
    print(c)
    n = int(input())
