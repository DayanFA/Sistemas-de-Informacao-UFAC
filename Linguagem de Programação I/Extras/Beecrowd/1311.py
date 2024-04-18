while True:
    S, B = map(int, input().split())
    if S == 0 and B == 0:
        break

    left = [i - 1 for i in range(S + 2)]
    right = [i + 1 for i in range(S + 2)]

    for _ in range(B):
        L, R = map(int, input().split())
        left[right[R]] = left[L]
        right[left[L]] = right[R]

        if left[L] == 0:
            print('*', end=' ')
        else:
            print(left[L], end=' ')
        
        if right[R] == S + 1:
            print('*')
        else:
            print(right[R])
    print('-')