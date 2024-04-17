import math

while True:
    n = int(input())
    if n == 0:
        break

    avg_g = n / 90.0
    bra = math.floor(avg_g * 1)
    ger = math.ceil(avg_g * 7)

    print("Brasil", bra, "x Alemanha", ger)