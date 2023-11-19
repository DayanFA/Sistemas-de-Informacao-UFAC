frase = "uma fr4se qu1 num sei9 aaa0"
sonu = {int(''.join(filter(str.isdigit, l))) for l in set(frase) if l.isdigit()}
print("Números:", sonu)

