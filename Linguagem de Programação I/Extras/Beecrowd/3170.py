B = int(input().strip())

G = int(input().strip())

needed_balls = G // 2

buy_balls = needed_balls - B

if buy_balls > 0:
    print(f'Faltam {buy_balls} bolinha(s)')
else:
    print('Amelia tem todas bolinhas!')