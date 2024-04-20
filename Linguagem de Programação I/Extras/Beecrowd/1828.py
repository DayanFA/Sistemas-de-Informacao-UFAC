wins = {
    'tesoura': ['papel', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'pedra': ['lagarto', 'tesoura'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}
T = int(input())
for t in range(1, T+1):
    sheldon, raj = input().split()
    if sheldon == raj:
        print(f'Caso #{t}: De novo!')
    elif raj in wins[sheldon]:
        print(f'Caso #{t}: Bazinga!')
    else:
        print(f'Caso #{t}: Raj trapaceou!')