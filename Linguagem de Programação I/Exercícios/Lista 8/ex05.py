def verifica(string):
    try:
        if not string.isalpha():
            raise ValueError("A string contém caracteres que não são letras.")
        if not string.isupper():
            raise ValueError("A string contém caracteres que não são maiúsculos.")
        print("A string é composta apenas por letras maiúsculas.")
    except ValueError as e:
        print("Erro:", e)

verifica("ABCDE")
verifica("ABcDE")
verifica("ABCD3")
