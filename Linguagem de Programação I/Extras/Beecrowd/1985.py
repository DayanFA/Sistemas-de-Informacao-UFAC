precos = {
    1001: 1.50,
    1002: 2.50,
    1003: 3.50,
    1004: 4.50,
    1005: 5.50
}

p = int(input())

total = 0

for _ in range(p):
    codigo, quantidade = map(int, input().split())
    
    total += precos[codigo] * quantidade

print(f'{total:.2f}')