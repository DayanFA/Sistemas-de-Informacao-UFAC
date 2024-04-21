while True:
    try:
        equation = input().split('=')
        if 'J' in equation[1]:
            R, L = map(int, equation[0].split('+'))
            print(R + L)
        elif 'L' in equation[0]:
            R = int(equation[0].split('+')[0])
            J = int(equation[1])
            print(J - R)
        else: 
            L = int(equation[0].split('+')[1])
            J = int(equation[1])
            print(J - L)
    except EOFError:
        break