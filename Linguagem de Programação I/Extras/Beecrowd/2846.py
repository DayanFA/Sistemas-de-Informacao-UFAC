def fibonot(k):
    fib = [1, 1]
    fibonot = []
    i = 2
    while len(fibonot) < k:
        fib.append(fib[i - 1] + fib[i - 2])
        for j in range(fib[i - 1] + 1, fib[i]):
            fibonot.append(j)
        i += 1
    return fibonot[k - 1]

k = int(input())
print(fibonot(k))