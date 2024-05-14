import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def intersects(x, y, w, h, cx, cy, r):
    dx = max(abs(cx - x - w / 2) - w / 2, 0)
    dy = max(abs(cy - y - h / 2) - h / 2, 0)
    return dx * dx + dy * dy <= r * r

T = int(input())
spells = {
    'fire': [(200, 20), (200, 30), (200, 50)],
    'water': [(300, 10), (300, 25), (300, 40)],
    'earth': [(400, 25), (400, 55), (400, 70)],
    'air': [(100, 18), (100, 38), (100, 60)]
}

for _ in range(T):
    w, h, x0, y0 = map(int, input().split())
    spell, level, cx, cy = input().split()
    level = int(level) - 1
    cx, cy = map(int, (cx, cy))
    damage, radius = spells[spell][level]
    if intersects(x0, y0, w, h, cx, cy, radius):
        print(damage)
    else:
        print(0)
