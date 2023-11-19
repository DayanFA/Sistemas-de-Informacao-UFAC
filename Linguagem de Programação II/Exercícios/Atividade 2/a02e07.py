import random

tuplas = [(n, random.randint(0, 100)) if n % 2 != 0 else (n, 'par') for n in range(1, 101)]
print(tuplas)
