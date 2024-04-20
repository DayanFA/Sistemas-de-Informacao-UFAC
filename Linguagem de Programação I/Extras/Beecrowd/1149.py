valores = list(map(int, input().split()))
a = valores.pop(0)
n = valores.pop(0)
while n <= 0:
    n = valores.pop(0)
print(a * n + (n * (n - 1)) // 2)