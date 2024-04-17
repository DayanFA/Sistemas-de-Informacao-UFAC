while True:
    try:
        N = int(input())

        R = [int(x) for x in input().strip().split(' ')]
        maria, joao = 0, 0

        for jogo in R:
            if(jogo == 0):
                maria += 1
            else:
                joao += 1
        
        print(f"Mary won {maria} times and John won {joao} times")
    except EOFError:
        break