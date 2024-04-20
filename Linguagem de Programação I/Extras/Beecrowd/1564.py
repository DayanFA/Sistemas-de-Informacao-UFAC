import sys

for line in sys.stdin:
    N = int(line.strip())
    if N == 0:
        print("vai ter copa!")
    else:
        print("vai ter duas!")