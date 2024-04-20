def solve():
    N = int(input())
    for _ in range(N):
        K, *O = map(int, input().split())
        O.sort(reverse=True)
        print(sum(O) - K + 1)

solve()