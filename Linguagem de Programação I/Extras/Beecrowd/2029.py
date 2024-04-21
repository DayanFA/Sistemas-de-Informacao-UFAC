while True:
    try:
        V = float(input())
        D = float(input())
        r = D / 2
        A = 3.14 * r * r
        H = V / A
        print("ALTURA = %.2f" % H)
        print("AREA = %.2f" % A)
    except EOFError:
        break