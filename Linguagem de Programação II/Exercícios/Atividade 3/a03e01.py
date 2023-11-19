def gera():
    s = [(0, 2), (1, 3), (2, 4), (4, 6), (5, 7)]
    for i in s:
        yield i
serie = gera()
print(list(serie))