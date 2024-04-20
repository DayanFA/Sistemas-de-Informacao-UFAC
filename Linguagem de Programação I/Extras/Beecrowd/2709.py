def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True

while True:
    try:
        M = int(input())
        coins = [int(input()) for _ in range(M)]
        N = int(input())
        sum_coins = sum(coins[::-N])
        if is_prime(sum_coins):
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except EOFError:
        break