n = int(input())
lightning_strikes = set()

for _ in range(n):
    x, y = map(int, input().split())
    if (x, y) in lightning_strikes:
        print(1)
        break
    lightning_strikes.add((x, y))
else:
    print(0)