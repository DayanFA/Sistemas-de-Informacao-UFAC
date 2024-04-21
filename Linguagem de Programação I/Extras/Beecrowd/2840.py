R, L = map(int, input().split())
volume = (4/3) * 3.1415 * (R**3)
balloons = int(L / volume)
print(balloons)