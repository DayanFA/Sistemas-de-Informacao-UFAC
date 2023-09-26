while True:
    try:
        a = list(input().split('-'))
        p = 'cobol'
        c = 0
        for i in range(5):
            if a[i][0].lower() == p[c]:
                c += 1
                if c == 5:
                    print('GRACE HOPPER')
                    break
            elif a[i][-1].lower() == p[c]:
                c += 1
                if c == 5:
                    print('GRACE HOPPER')
                    break
        else:
            print('BUG')
    except EOFError:
        break
