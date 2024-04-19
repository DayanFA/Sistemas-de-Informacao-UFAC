N = int(input())
H = list(map(int, input().split()))

if any(H[i] == H[i-1] for i in range(1, N)):
    print(0)
else:
    pattern = [1 if H[i] > H[i-1] else 0 for i in range(1, N)]
    result = all(pattern[i] != pattern[i-1] for i in range(1, N-1))
    print(int(result))