def imprimir(*args, **kwargs):
    print("Argumentos posicionais na ordem inversa:")
    for arg in reversed(args):
        print(arg)

    print("\nArgumentos nomeados em ordem alfabética:")
    for key, value in sorted(kwargs.items()):
        print(f"{key}: {value}")

imprimir(3, 'b', 1, Nome='Júnior', Sobrenome='Limeira', Idade=29, Profissao='Professor')
