N = int(input())
K = int(input())
scores = [int(input()) for _ in range(N)]

scores.sort(reverse=True)
last_score = scores[K-1]

qualified = sum(1 for score in scores if score >= last_score)

print(qualified)