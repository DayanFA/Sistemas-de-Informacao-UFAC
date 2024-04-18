while True:
    try:
        V, N = input().split()
        V = float(V)
        N = int(N)
        share = V / N
        print("{:.2f}".format(share))
    except EOFError:
        break