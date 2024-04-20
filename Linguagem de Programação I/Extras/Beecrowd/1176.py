fib = [0] * 61
fib[1] = 1
for i in range(2, 61):
    fib[i] = fib[i-1] + fib[i-2]
T = int(input())
for _ in range(T):
    N = int(input())
    print(f'Fib({N}) = {fib[N]}')