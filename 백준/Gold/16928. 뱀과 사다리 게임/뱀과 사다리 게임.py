import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs():
    visited = [False] * 101
    visited[1] = True
    queue = deque([(1, 0)])
    while queue:
        x, time = queue.popleft()
        if x == 100:
            return time
        for dx in [6, 5, 4, 3, 2, 1]:
            nx = x + dx
            if 0 < nx < 101:
                if nx in ladder.keys():
                    queue.append((ladder[nx], time + 1))
                    visited[ladder[nx]] = True
                elif nx in snake.keys():
                    queue.append((snake[nx], time + 1))
                    visited[snake[nx]] = True
                elif not visited[nx]:
                    queue.append((nx, time + 1))
                    visited[nx] = True
    return -1


# 입력
n, m = map(int, input().split())  # n : 사다리 수, m : 뱀의 수

ladder = {}  # 사다리 정보
for _ in range(n):
    x, y = map(int, input().split())  # x번 칸에 도착하면 y번 칸으로 이동
    ladder[x] = y

snake = {}  # 뱀 정보
for _ in range(m):  # 뱀 정보
    u, v = map(int, input().split())  # u번 칸에 도착하면, v번 칸으로 이동
    snake[u] = v

print(bfs())
