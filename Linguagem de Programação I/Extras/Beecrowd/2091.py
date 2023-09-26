while True:
    n = int(input())
    if n== 0:
        break
    v = list(map(int, input().split()))
    r= 0
    for i in v:
        r ^=i
    print(r)