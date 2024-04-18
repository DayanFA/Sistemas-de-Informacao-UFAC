n = int(input())
win_count = 0

for _ in range(n):
    battle = input()
    if 'CD' not in battle:
        win_count += 1

print(win_count)