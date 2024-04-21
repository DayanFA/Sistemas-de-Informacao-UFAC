def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_super(n):
    prime_digits = {'2', '3', '5', '7'}
    return all(digit in prime_digits for digit in str(n))

while True:
    try:
        n = int(input())
        if is_prime(n):
            if is_super(n):
                print('Super')
            else:
                print('Primo')
        else:
            print('Nada')
    except EOFError:
        break