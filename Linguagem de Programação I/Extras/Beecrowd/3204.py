dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]

def solve():
    dp = [[[0]*15 for _ in range(15)] for _ in range(15)]
    dp[7][7][0] = 1
    for k in range(1, 15):
        for i in range(15):
            for j in range(15):
                for d in range(6):
                    x, y = i + dx[d], j + dy[d]
                    if 0 <= x < 15 and 0 <= y < 15:
                        dp[i][j][k] += dp[x][y][k-1]
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(dp[7][7][n])

solve()