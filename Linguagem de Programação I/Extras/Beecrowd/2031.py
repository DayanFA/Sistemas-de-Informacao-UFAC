def determine_winner():
    N = int(input())
    for _ in range(N):
        player1 = input()
        player2 = input()
        if player1 == player2:
            if player1 == "ataque":
                print("Aniquilacao mutua")
            elif player1 == "pedra":
                print("Sem ganhador")
            else:
                print("Ambos venceram")
        else:
            if player1 == "ataque" or (player1 == "pedra" and player2 != "ataque"):
                print("Jogador 1 venceu")
            else:
                print("Jogador 2 venceu")

determine_winner()