def max_consecutive_ones(n):
    return max(map(len, bin(n)[2:].split('0')))

N = int(input())
for _ in range(N):
    X = int(input())
    print(max_consecutive_ones(X))