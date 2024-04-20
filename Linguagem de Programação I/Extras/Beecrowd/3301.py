while True:
    try:
        ages = list(map(int, input().split()))
        names = ['huguinho', 'zezinho', 'luisinho']
        mapping = dict(zip(ages, names))
        ages.sort()
        print(mapping[ages[1]])
    except EOFError:
        break