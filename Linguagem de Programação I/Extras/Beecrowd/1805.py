def sum_natural_numbers(n):
    return n * (n + 1) // 2

while True:
    try:
        A, B = map(int, input().split())
    except EOFError:
        break

    sum_A = sum_natural_numbers(A - 1)
    sum_B = sum_natural_numbers(B)
    print(sum_B - sum_A)