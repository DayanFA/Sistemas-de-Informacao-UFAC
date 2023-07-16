n = int(input())
forca = [4, 5, 6, 7, 12, 11, 13, 1, 2, 3]
aws = 0
bws = 0

for _ in range(n):
    partida = input().split()
    arw = 0
    brw = 0

    for i in range(3):
        if forca.index(int(partida[i])) > forca.index(int(partida[i + 3])) or forca.index(int(partida[i])) == forca.index(int(partida[i + 3])):
            arw += 1
        else:
            brw += 1

    if arw > brw or arw == brw:
        aws += 1
    else:
        bws += 1

print(aws, bws)