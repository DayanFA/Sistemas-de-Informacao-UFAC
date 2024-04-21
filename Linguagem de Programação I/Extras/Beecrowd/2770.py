import sys

for line in sys.stdin:
    X, Y, M = map(int, line.split())
    for _ in range(M):
        Xi, Yi = map(int, sys.stdin.readline().split())
        if (Xi <= X and Yi <= Y) or (Xi <= Y and Yi <= X):
            print("Sim")
        else:
            print("Nao")