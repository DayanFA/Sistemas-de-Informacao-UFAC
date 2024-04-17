import sys

def longest_common_substring(A, B):
    n, m = len(A), len(B)
    T = [[0] * (m + 1) for _ in range(n + 1)]
    result = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
                result = max(result, T[i][j])

    return result

for line in sys.stdin:
    A = line.strip()
    B = next(sys.stdin).strip()
    print(longest_common_substring(A, B))