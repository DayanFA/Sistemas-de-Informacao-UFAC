N, M = map(int, input().split())
terrain = [list(map(int, input().split())) for _ in range(N)]

def is_lightsaber(i, j):
    if terrain[i][j] == 42:
        for dx, dy in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
            if terrain[i + dx][j + dy] != 7:
                return False
        return True
    return False

for i in range(1, N-1):
    for j in range(1, M-1):
        if is_lightsaber(i, j):
            print(i+1, j+1)
            exit(0)

print(0, 0)