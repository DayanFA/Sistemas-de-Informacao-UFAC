def fib(n):
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a

n = int(input("Digite o valor de n para o termo desejado na série de Fibonacci: "))
result = fib(n)
print(f"O {n}-ésimo termo na série de Fibonacci é: {result}")
