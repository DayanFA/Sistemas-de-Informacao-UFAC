# Atividade 1

with open('entrada1.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Olá, mundo!')

class VogalSubstituidora:
    def substituir_vogais(self, arquivo_entrada, arquivo_saida):
        with open(arquivo_entrada, 'r', encoding='utf-8') as entrada, open(arquivo_saida, 'w', encoding='utf-8') as saida:
            for linha in entrada:
                for vogal in 'aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãõÃÕ':
                    linha = linha.replace(vogal, '*')
                saida.write(linha)

substituidora = VogalSubstituidora()
substituidora.substituir_vogais('entrada1.txt', 'saida1.txt')

# Atividade 2

with open('entrada2.txt', 'w') as arquivo:
    arquivo.write('\n'.join(map(str, [5, 3, 2, 8, 6])))

class OrdenadorDeNumeros:
    def ordenar_numeros(self, arquivo_entrada, arquivo_saida):
        with open(arquivo_entrada, 'r') as entrada:
            numeros = [int(linha) for linha in entrada]
        numeros.sort()
        with open(arquivo_saida, 'w') as saida:
            saida.write('\n'.join(map(str, numeros)))

ordenador = OrdenadorDeNumeros()
ordenador.ordenar_numeros('entrada2.txt', 'saida2.txt')

# Atividade 3

import string

class ContadorDeCaracteristicas:
    def contar_caracteristicas(self, *arquivos):
        for arquivo in arquivos:
            with open(arquivo, 'r', encoding='utf-8') as f:
                texto = f.read()
            vogais = sum(1 for char in texto if char.lower() in 'aeiouáéíóúâêîôûãõ')
            consoantes = sum(1 for char in texto if char.lower() in string.ascii_letters and char.lower() not in 'aeiouáéíóúâêîôûãõ')
            especiais = sum(1 for char in texto if not char.isalnum() and not char.isspace())
            palavras = sum(1 for palavra in texto.split() if palavra.isalpha())
            linhas = texto.count('\n') + 1
            print(f'Arquivo: {arquivo}\nVogais: {vogais}\nConsoantes: {consoantes}\nEspeciais: {especiais}\nPalavras: {palavras}\nLinhas: {linhas}\n')

contador = ContadorDeCaracteristicas()
contador.contar_caracteristicas('entrada1.txt', 'entrada2.txt')

# Atividade 4

class VerificadorDeIgualdade:
    def verificar_igualdade(self, arquivo1, arquivo2):
        with open(arquivo1, 'r', encoding='utf-8') as f1, open(arquivo2, 'r', encoding='utf-8') as f2:
            return f1.read() == f2.read()

verificador = VerificadorDeIgualdade()
print(verificador.verificar_igualdade('entrada1.txt', 'entrada2.txt'))

# Atividade 5

class SubstituidorDeString:
    def substituir_string(self, string_padrao, string_substituicao, arquivo_entrada, arquivo_saida):
        with open(arquivo_entrada, 'r', encoding='utf-8') as entrada, open(arquivo_saida, 'w', encoding='utf-8') as saida:
            for linha in entrada:
                saida.write(linha.replace(string_padrao, string_substituicao))

substituidor = SubstituidorDeString()
substituidor.substituir_string('mundo', 'planeta', 'entrada1.txt', 'saida3.txt')

# Atividade 6

class CalculadorDeMedia:
    def criar_arquivos(self, nomes, notas):
        with open('nomes.txt', 'w', encoding='utf-8') as f:
            for nome in nomes:
                f.write(f'{nome}\n')
        with open('notas.txt', 'w', encoding='utf-8') as f:
            for nota in notas:
                f.write(' '.join(map(str, nota)) + '\n')

    def calcular_media(self, arquivo_nomes, arquivo_notas, arquivo_saida):
        with open(arquivo_nomes, 'r', encoding='utf-8') as nomes, open(arquivo_notas, 'r', encoding='utf-8') as notas, open(arquivo_saida, 'w', encoding='utf-8') as saida:
            for nome, nota in zip(nomes, notas):
                media = sum(map(float, nota.split())) / len(nota.split())
                saida.write(f'{nome.strip()}: {media}\n')

calculador = CalculadorDeMedia()
calculador.criar_arquivos(['João', 'Maria', 'Pedro'], [[7.5, 8.5], [9.0, 9.5], [8.0, 7.0]])
calculador.calcular_media('nomes.txt', 'notas.txt', 'medias.txt')

# Atividade 7

class CalculadorDeMedia:
    def imprimir_medias(self, arquivo_medias):
        with open(arquivo_medias, 'r', encoding='utf-8') as f:
            medias = [linha.strip() for linha in f]
        medias.sort(key=lambda x: float(x.split(': ')[1]), reverse=True)
        for media in medias:
            print(media)

calculador = CalculadorDeMedia()
calculador.imprimir_medias('medias.txt')
