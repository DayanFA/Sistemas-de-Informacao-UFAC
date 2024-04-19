N = int(input().strip())

for _ in range(N):
    S = input().strip()

    Q = int(input().strip())

    for _ in range(Q):
        R = input().strip()

        index_S = 0

        for char in R:
            index_S = S.find(char, index_S) + 1
            if index_S == 0:
                break

        if index_S != 0:
            print("Yes")
        else:
            print("No")