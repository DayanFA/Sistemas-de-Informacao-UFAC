while True:
    try:
        A, B, C = [int(x) for x in input().strip().split(' ')]

        if(A + B + C == 1):
            if(A == 1):
                print('A')
            if(B == 1):
                print('B')
            if(C == 1):
                print('C')
        elif(A + B + C == 2):
            if(A == 0):
                print('A')
            if(B == 0):
                print('B')
            if(C == 0):
                print('C')
        else:
            print('*')
    except EOFError:
        break