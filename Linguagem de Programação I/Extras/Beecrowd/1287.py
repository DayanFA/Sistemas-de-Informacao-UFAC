while True:
    try:
        s = input()
    except EOFError:
        break

    s = s.replace('O', '0').replace('o', '0').replace('l', '1').replace(',', '').replace(' ', '')

    if not s.isdigit() or int(s) > 2147483647:
        print('error')
    else:
        print(int(s))