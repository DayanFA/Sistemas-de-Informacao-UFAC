def imprimir(**kwargs):
    if 'Nome' in kwargs and 'Idade' in kwargs:
        print(f"Nome: {kwargs['Nome']} Idade: {kwargs['Idade']}")

imprimir(Nome='Júnior', Sobrenome='Limeira', Idade=29, Profissao='Professor')

