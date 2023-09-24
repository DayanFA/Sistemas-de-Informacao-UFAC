class FahrenheitError(Exception):
    pass

def converte(f):
    if f < -459.67:
        raise FahrenheitError("A temperatura em Fahrenheit não pode ser menor que -459.67°F")
    c = 5 * (f - 32) / 9
    return c

try:
    f = float(input(""))
    c = converte(f)
    print("A temperatura em Celsius é:", c)
except FahrenheitError as e:
    print("Erro:", e)
except ValueError:
    print("Erro: O valor inserido não é um número válido em Fahrenheit.")
