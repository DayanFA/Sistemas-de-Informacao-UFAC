N, M = map(int, input().split())
keyboard = {}
for _ in range(N):
    E, S = input().split()
    keyboard[E] = S
    keyboard[S] = E
for _ in range(M):
    phrase = input()
    corrected_phrase = ''.join(keyboard.get(ch, ch) for ch in phrase)
    print(corrected_phrase)