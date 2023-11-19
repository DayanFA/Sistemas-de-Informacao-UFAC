frase = "Algo com consoante e não vogal"
consoantes = [l for l in frase if l.isalpha() and l.lower() not in 'aeiou']
print(consoantes)
