N = int(input())

for _ in range(N):
    QT, S = map(int, input().split())
    values = list(map(int, input().split()))

    closest_diff = float('inf')
    winner = 1
    for i in range(QT):
        diff = abs(values[i] - S)
        if diff < closest_diff or (diff == closest_diff and i + 1 < winner):
            closest_diff = diff
            winner = i + 1

    print(winner)
