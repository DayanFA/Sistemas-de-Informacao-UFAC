while True:
    d, n = input().split()
    if d == '0' and n == '0':
        break
    n = list(n)
    while d in n:
        n.remove(d)
    if n == []:
        print(0)
    else:
        n = ''.join(n)
        print(int(n))