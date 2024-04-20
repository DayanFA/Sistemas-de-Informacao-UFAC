import sys

for line in sys.stdin:
    N = int(line)
    votes = list(map(int, input().split()))
    if votes.count(1) >= (2/3) * N:
        print("impeachment")
    else:
        print("acusacao arquivada")