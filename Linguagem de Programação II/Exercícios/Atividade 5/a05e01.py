def multifor(*args):
    r = 1
    for i in args:
        r *= i
    return r

from functools import reduce

def multired(*args):
    return reduce(lambda x, y: x * y, args)

n = 7, 9, 24, 5
resultfor = multifor(*n)
resultred = multired(*n)

print(f'Resultado usando o laço for: {resultfor}')
print(f'Resultado usando reduce: {resultred}')
