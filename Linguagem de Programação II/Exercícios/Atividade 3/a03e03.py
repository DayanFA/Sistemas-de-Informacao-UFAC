import random
def mega():
    for _ in range(6):
        yield random.randint(1, 60)

megasena = mega()
print(list(megasena))