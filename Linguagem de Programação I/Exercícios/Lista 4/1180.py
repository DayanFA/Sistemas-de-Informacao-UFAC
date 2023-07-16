N = int(input())

X = list(map(int, input().split()))

min_value = min(X)
min_position = X.index(min_value)

print("Menor valor:", min_value)
print("Posicao:", min_position)