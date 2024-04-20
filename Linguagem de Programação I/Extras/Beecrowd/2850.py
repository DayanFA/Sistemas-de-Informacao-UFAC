import sys

for line in sys.stdin:
    line = line.strip()
    if line == "esquerda":
        print("ingles")
    elif line == "direita":
        print("frances")
    elif line == "nenhuma":
        print("portugues")
    elif line == "as duas":
        print("caiu")