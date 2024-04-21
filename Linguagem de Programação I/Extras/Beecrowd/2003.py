import sys

for line in sys.stdin:
    h, m = map(int, line.strip().split(':'))
    if h == 7:
        print(f'Atraso maximo: {m}')
    elif h == 8:
        print(f'Atraso maximo: {60 + m}')
    elif h == 9:
        print(f'Atraso maximo: {120 + m}')
    else:
        print('Atraso maximo: 0')