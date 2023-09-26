p = {3: 'terno', 4: 'quadra', 5: 'quina', 6: 'sena'}
n = list(map(int, input().split()))
s = list(map(int, input().split()))
n = set(n)
s = set(s)
c = set(n & s)
if len(c) < 3:
    print('azar')
else:
    print(p[len(c)])