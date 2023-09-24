t = 0

while t < 3:
    try:
        v = float(input("Digite um valor real: "))
        print("Valor digitado:", v)
        break
    except ValueError:
        t += 1
        if t == 3:
            print("Você excedeu o limite de tentativas.")
        else:
            print("Valor inválido. Tente novamente.")
