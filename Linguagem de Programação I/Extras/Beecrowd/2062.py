n = int(input())
a = input().split()
c = ''
for i in range(n):
    b = a[i]
    if b[:-1] == 'OB':
        c += 'OBI '
    elif b[:-1] == 'UR':
        c += 'URI '
    else:
        c += b + ' '
print(c.strip())