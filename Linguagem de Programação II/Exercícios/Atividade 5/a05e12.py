def cord(i, j, k, n):
    coordenadas = [(x, y, z) for x in range(i + 1) for y in range(j + 1) for z in range(k + 1) if x + y + z != n]
    return coordenadas

i, j, k, n = 1, 1, 2, 3
val = cord(i, j, k, n)
print(val)
