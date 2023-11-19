frase = "Um exemplo qualquer de frase"
result = list(map(lambda x: (len(x), sum(1 for char in x if char.lower() in 'aeiou')), frase.split()))
print(result)
