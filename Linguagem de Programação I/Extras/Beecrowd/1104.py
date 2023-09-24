while True:
    try:
        a, b = map(int, input().strip().split(' '))
        al = set(map(int, input().strip().split(' ')))
        be = set(map(int, input().strip().split(' ')))
        u = al | be
        print(min(len(u) - len(be), len(u) - len(al)))
    except EOFError:
        break
