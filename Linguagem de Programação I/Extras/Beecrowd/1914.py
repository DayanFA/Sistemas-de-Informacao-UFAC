QT = int(input())
for _ in range(QT):
    player1, choice1, player2, choice2 = input().split()
    N, M = map(int, input().split())
    if (N + M) % 2 == 0:
        if choice1 == "PAR":
            print(player1)
        else:
            print(player2)
    else:
        if choice1 == "IMPAR":
            print(player1)
        else:
            print(player2)