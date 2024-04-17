import sys

n = int(sys.stdin.readline())
carneiros = list(map(int, sys.stdin.readline().split()))

estrelas_atacadas = [False]*n
i = 0
while 0 <= i < n:
    estrelas_atacadas[i] = True
    if carneiros[i] % 2 == 0:
        carneiros[i] = max(carneiros[i] - 1, 0)
        i -= 1
    else:
        carneiros[i] = max(carneiros[i] - 1, 0)
        i += 1

sys.stdout.write(str(estrelas_atacadas.count(True)) + " " + str(sum(carneiros)) + "\n")