import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()


def bfs(n, k):
    visited = [False] * 100_002
    queue = deque([(n, 0)])
    while queue:
        x, time = queue.popleft()
        if x == k:
            return time
        for dx in [1, -1]:
            nx = x + dx
            if 0 <= nx < 100_002 and not visited[nx]:
                queue.append((nx, time + 1))
                visited[nx] = True
        nx = x * 2
        if 0 <= nx < 100_002 and not visited[nx]:
            queue.append((nx, time + 1))
            visited[nx] = True

    return 1


# 입력
n, k = map(int, input().split())

print(bfs(n, k))
