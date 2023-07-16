i = 1
j = 60
while j > 0:
    for a in range(60,0,-1):
        print('I={} J={}'.format(i, j))
        j -=5
        i +=3
        if j < 0:
            break