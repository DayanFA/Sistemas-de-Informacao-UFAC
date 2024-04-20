import math

while True:
    inputs = list(map(int, input().split()))
    if inputs[0] == 0:
        break

    A, B, C = inputs
    area = A * B
    land_area = (area * 100) / C
    land_side = math.sqrt(land_area)
    print(int(land_side))