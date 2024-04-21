P, N = map(int, input().split())
canos = list(map(int, input().split()))

for i in range(N - 1):
    if abs(canos[i] - canos[i + 1]) > P:
        print("GAME OVER")
        break
else:
    print("YOU WIN")