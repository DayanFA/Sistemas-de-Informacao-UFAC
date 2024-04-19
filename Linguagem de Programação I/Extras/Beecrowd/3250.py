from collections import deque

def bfs(f, s, g, u, d):
    visited = [False] * (f + 1)
    distance = [0] * (f + 1)
    queue = deque([s])
    visited[s] = True

    while queue:
        current = queue.popleft()
        if current == g:
            return distance[current]
        if current + u <= f and not visited[current + u]:
            queue.append(current + u)
            visited[current + u] = True
            distance[current + u] = distance[current] + 1
        if current - d >= 1 and not visited[current - d]:
            queue.append(current - d)
            visited[current - d] = True
            distance[current - d] = distance[current] + 1

    return "use the stairs"

f, s, g, u, d = map(int, input().split())
print(bfs(f, s, g, u, d))