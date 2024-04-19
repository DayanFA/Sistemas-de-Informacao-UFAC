import sys

for line in sys.stdin:
    dodo, leo, pepper = line.split()
    if (dodo == 'pedra' and leo == 'tesoura' and pepper == 'tesoura') or \
       (dodo == 'papel' and leo == 'pedra' and pepper == 'pedra') or \
       (dodo == 'tesoura' and leo == 'papel' and pepper == 'papel'):
        print("Os atributos dos monstros vao ser inteligencia, sabedoria...")
    elif (leo == 'pedra' and dodo == 'tesoura' and pepper == 'tesoura') or \
         (leo == 'papel' and dodo == 'pedra' and pepper == 'pedra') or \
         (leo == 'tesoura' and dodo == 'papel' and pepper == 'papel'):
        print("Iron Maiden's gonna get you, no matter how far!")
    elif (pepper == 'pedra' and dodo == 'tesoura' and leo == 'tesoura') or \
         (pepper == 'papel' and dodo == 'pedra' and leo == 'pedra') or \
         (pepper == 'tesoura' and dodo == 'papel' and leo == 'papel'):
        print("Urano perdeu algo muito precioso...")
    else:
        print("Putz vei, o Leo ta demorando muito pra jogar...")