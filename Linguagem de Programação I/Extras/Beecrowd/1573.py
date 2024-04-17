import math

while True:
    try:
        A, B, C = [int(x) for x in input().strip().split(' ')]

        if(A == 0 and B == 0 and C == 0):
            break

        print(math.floor((A * B * C)**(1.0/3.0)))
    except EOFError:
        break