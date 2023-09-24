class RespostaInvalidaError(Exception):
    pass

def confirma():
    while True:
        r = input().lower()
        if r == 'sim':
            return True
        elif r == 'não':
            return False
        else:
            raise RespostaInvalidaError("Resposta inválida")

try:
    r = confirma()
    print("Tudo certo = ", r)
except RespostaInvalidaError as e:
    print("Erro:", e)
