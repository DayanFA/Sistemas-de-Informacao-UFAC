n = int(input())
ant1 = 0
ant2 = 1
fib = [ant1, ant2]
for _ in range(n - 2):
    prox = ant1 + ant2
    fib.append(prox)
    ant1, ant2 = ant2, prox
print(" ".join(str(num) for num in fib))

