import sys

for line in sys.stdin:
    if line.strip().isdigit():
        continue
    speeds = list(map(int, line.split()))
    max_speed = max(speeds)
    if max_speed < 10:
        print(1)
    elif max_speed < 20:
        print(2)
    else:
        print(3)