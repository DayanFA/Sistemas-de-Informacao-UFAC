fatura = [('Net', 199.9), ('Ifood', 999.87), ('Gasolina', 678.0), ('Formigão', 400)]

print("Imprimir no formato ‘Tipo de gasto’ – R$ valor e Ordenar os itens por valor:")
fatura.sort(key=lambda x: x[1])
for i in fatura:
    print(f"{i[0]} - R$ {i[1]}")

print("\nFiltrar os gastos acima de R$ 500:")
gastoacima = list(filter(lambda x: x[1] > 500, fatura))
for i in gastoacima:
    print(f"{i[0]} - R$ {i[1]}")

total = sum(i[1] for i in fatura)
print(f"\nApresentar o total da fatura: R$ {total}")

#usando o args
def soma(*args):
    r = 0
    for i in args:
        r += i
    return r

valor = list(map(lambda x: x[1], fatura))
total = soma(*valor)
print(f"\nApresentar o total da fatura: R$ {total}")