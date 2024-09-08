import sys
from collections import deque

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

result = []

for _ in range(int(input())):
    K = int(input())
    x_start, y_start = map(int, input().split())
    x_end, y_end = map(int, input().split())

    queue = deque()
    queue.append((x_start, y_start))

    graph = [[-1] * K for _ in range(K)]
    graph[x_start][y_start] = 0

    while queue:
        x, y = queue.popleft()
        for j in range(8):
            nx = x + dx[j]
            ny = y + dy[j]

            if nx < 0 or nx >= K or ny < 0 or ny >= K:
                continue

            if graph[nx][ny] != -1:
                continue

            graph[nx][ny] = graph[x][y] + 1
            queue.append((nx, ny))

        if graph[x_end][y_end] != -1:
            break

    result.append(graph[x_end][y_end])

for r in result:
    print(r)