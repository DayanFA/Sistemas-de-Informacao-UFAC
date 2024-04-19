C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    power = N ** M
    digits = len(str(power))
    print(digits)