while True:
    try:
        a, letras = list(input().split('-')), []
        palavra = 'cobol'
        cont = 0
        for i in range(5):
            if a[i][0].lower() == palavra[cont]:
                cont += 1
                if cont == 5:
                    print('GRACE HOPPER')
                    break
            elif a[i][-1].lower() == palavra[cont]:
                cont += 1
                if cont == 5:
                    print('GRACE HOPPER')
                    break
        else:
            print('BUG')
    except EOFError:
        break
