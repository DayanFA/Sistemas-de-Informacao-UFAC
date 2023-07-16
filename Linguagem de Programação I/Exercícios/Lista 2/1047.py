sh, sm, eh, em = map(int, input().split())
st = sh * 60 + sm
et = eh * 60 + em
d = et - st
if d <= 0:
    d += 24 * 60
h = d // 60
m = d % 60
print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)' .format(h,m))

