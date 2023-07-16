n = int(input())
g=0
while True:
    k= 0
    g += 1
    x= float(input())
    while x > 1:
        x = x / 2
        k += 1
    print('{} dias' .format(k))
    if g == n:
        break