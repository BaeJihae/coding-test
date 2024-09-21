import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map_data[nx][ny] == 1:
                visited[nx][ny] = True
                queue.append((nx, ny))

    return 1


for tc in range(int(input())):
    m, n, k = map(int, input().split())
    map_data = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        map_data[y][x] = 1

    visited = [[False] * m for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and map_data[i][j] == 1:
                answer += bfs(i, j)

    print(answer)
