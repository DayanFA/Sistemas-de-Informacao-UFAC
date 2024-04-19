def is_difficult(surname):
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    count = 0
    for char in surname:
        if char in consonants:
            count += 1
            if count >= 3:
                return True
        else:
            count = 0
    return False

N = int(input().strip())
for _ in range(N):
    surname = input().strip()
    if is_difficult(surname):
        print(f'{surname} nao eh facil')
    else:
        print(f'{surname} eh facil')