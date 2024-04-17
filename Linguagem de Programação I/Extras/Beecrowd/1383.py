from functools import reduce

def verificaLinha(sudoku, x):
    numeros = set(sudoku[x])
    return len(numeros) == 9

def verificaColuna(sudoku, x):
    numeros = set([sudoku[i][x] for i in range(9)])
    return len(numeros) == 9

def verificaQuadrado(sudoku, x):
    linha, coluna = 3*(x//3), 3*(x%3)
    numeros = set(list(reduce(list.__add__, [l[coluna:(coluna + 3)] for l in sudoku[linha:(linha + 3)]])))
    return len(numeros) == 9

n = int(input())
for k in range(1, n + 1):
    sudoku = []

    for i in range(9):
        sudoku.append([int(x) for x in input().strip().split(' ')])
    
    print(f"Instancia {k}")

    resposta = "SIM"
    for i in range(9):
        if(not verificaLinha(sudoku, i) or not verificaColuna(sudoku, i) or not verificaQuadrado(sudoku, i)):
            resposta = "NAO"
    
    print(resposta)
    print()