import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(i, j, n, visited, map_data):
    queue = deque([(i, j)])
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and map_data[nx][ny] == '1' and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt



# 입력
n = int(input())
map_data = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]  # 방문 체크를 위한 배열
house_cnt_lst = []  # 단지에 속하는 집의 수

# 단지 개수 세아리기
for i in range(n):
    for j in range(n):
        if not visited[i][j] and map_data[i][j] == '1':
            visited[i][j] = True
            house_cnt_lst.append(bfs(i, j, n, visited, map_data))

print(len(house_cnt_lst))
[print(i) for i in sorted(house_cnt_lst)]