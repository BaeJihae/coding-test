import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(i, j, n, visited, painting):
    queue = deque([(i, j)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and painting[x][y] == painting[nx][ny] and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return 1


# 입력
n = int(input())
painting = [list(input()) for _ in range(n)]

visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 체크를 위한 배열
person = 0  # 적록색약이 아닌 사람의 구역수
# 적록색약이 아닌 사람의 구역 세기
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            person += bfs(i, j, n, visited, painting)

# 초록 구역을 빨강 구역으로 바꾸기
for i in range(n):
    for j in range(n):
        if painting[i][j] == 'G':
            painting[i][j] = 'R'

visited = [[False for _ in range(n)] for _ in range(n)]  # 방문 체크를 위한 배열
red_green_medicine_person = 0  # 적록색약인 사람의 구역수
# 적록색약인 사람의 구역 세기
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            red_green_medicine_person += bfs(i, j, n, visited, painting)

# 출력
print(person, red_green_medicine_person)