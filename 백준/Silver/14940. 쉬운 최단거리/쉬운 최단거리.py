import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())
map_data = [list(map(int, input().split())) for _ in range(n)]

# 목표지점 찾기
start_x, start_y = 0, 0
# 갈 수 없는 땅 표시해두기
ob_list = []

for i in range(n):
    for j in range(m):
        if map_data[i][j] == 2:
            start_x, start_y = i, j
        if map_data[i][j] == 0:
            ob_list.append((i, j))

def bfs(new_map):
    visited = [[False] * m for _ in range(n)]
    queue = deque([(start_x, start_y)])
    distance = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.popleft()
            new_map[x][y] = distance
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and map_data[nx][ny] == 1 and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
        distance += 1

    return new_map

new_map_data = bfs([[-1] * m for _ in range(n)])

for x, y in ob_list:
    new_map_data[x][y] = 0

for row in new_map_data:
    print(*row)
