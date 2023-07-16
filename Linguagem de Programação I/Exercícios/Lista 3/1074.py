N = int(input())
for _ in range(N):
    x = int(input())
    if x == 0:
        print('NULL')
    elif x % 2 == 0:
        if x > 0:
            print('EVEN POSITIVE')
        elif x < 0:
            print('EVEN NEGATIVE')
    elif x % 2 != 0:
        if x > 0:
            print('ODD POSITIVE')
        elif x < 0:
            print('ODD NEGATIVE')