while True:
    try:
        n = int(input())
        fastest = min(float(input()) for _ in range(n))
        print(f'{fastest:.2f}')
    except EOFError:
        break