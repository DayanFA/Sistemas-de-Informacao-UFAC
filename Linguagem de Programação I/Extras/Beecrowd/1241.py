try:
    n = int(input())
    for _ in range(n):
        a,b = input().split()
        c = 0
        if len(a) > len(b):
            a, b = b, a
        for i in range(len(a)):
            if a[len(a) - 1 - i] == b[len(b) - 1 - i]:
                c += 1
        if c == len(a):
            print('encaixa')
        else:
            print('nao encaixa')
except EOFError:
    pass