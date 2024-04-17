import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, direction):
        if direction == 'C': self.y += 1
        elif direction == 'B': self.y -= 1
        elif direction == 'E': self.x -= 1
        elif direction == 'D': self.x += 1

    def dist(self, other):
        return (self.x - other.x)**2 + (self.y - other.y)**2

    def reached(self, other):
        return self.dist(other) == 0

    def exceeded(self, other, k):
        return self.dist(other) >= k

    def done(self, other, k):
        return self.reached(other) or self.exceeded(other, k)

def when_trap(target, k):
    current = Point()
    for i, direction in enumerate(instructions):
        if current.done(target, k): break
        current.move(direction)
    return -1 if current.reached(target) else min(i + 1, len(instructions))

n, k, x, y = map(int, input().split())
k *= k
target = Point(x, y)

instructions = [input().strip() for _ in range(n)]

result = when_trap(target, k)

if result == -1:
    print('Sucesso')
else:
    print(f'Trap {result}')