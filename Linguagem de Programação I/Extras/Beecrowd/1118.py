n = 0
while True:
    x= float(input())
    if x< 0 or x>10:
        print('nota invalida')
    elif x >= 0 or x <= 10:
        n1 = x
        if n == 0:
            n += 1
            n2 = n1
        else:
            n += 1
    if n == 2:
        m = (n1 + n2)/ 2.0
        print('media = {:.2f}' .format(m))
        while True:
            print('novo calculo (1-sim 2-nao)')
            x = float(input())
            if x == 1 or x == 2:
                break
    if x == 1:
        n = 0
        continue
    if x == 2:
        break