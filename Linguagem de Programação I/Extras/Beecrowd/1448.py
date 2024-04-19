t = int(input())
for i in range(1, t+1):
    correct = input()
    team1 = input()
    team2 = input()

    score1 = sum(c1 == c2 for c1, c2 in zip(correct, team1))
    score2 = sum(c1 == c2 for c1, c2 in zip(correct, team2))

    print('Instancia', i)
    if score1 > score2:
        print('time 1')
    elif score1 < score2:
        print('time 2')
    else:
        for c1, c2, c3 in zip(correct, team1, team2):
            if c1 == c2 and c1 != c3:
                print('time 1')
                break
            elif c1 != c2 and c1 == c3:
                print('time 2')
                break
        else:
            print('empate')
    print()