st,et=map(int, input().split())
d=et-st
if d <= 0:
    d += 24
print('O JOGO DUROU {} HORA(S)'.format(d))