v = input()
s = v.split(',')
vv = []
for x in s:
    try:
        k = int(x)
        vv.append(k)
    except ValueError:
        print(f"O valor '{x}' não pôde ser convertido para um número inteiro.")

print("Valores convertidos para inteiros:", vv)
