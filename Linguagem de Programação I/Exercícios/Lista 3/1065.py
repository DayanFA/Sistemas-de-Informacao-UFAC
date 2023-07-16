ec= 0
for _ in range(5):
    v = int(input())
    if v % 2 == 0:
        ec += 1
print('{} valores pares'.format(ec))
