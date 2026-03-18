# 너비 우선 탐색 
from collections import deque

node = [[], [2, 3], [5, 6], [4], [6], [], []]

v = 6 # 노드의 개수
e = 6 # 에지의 개수

queue = deque()
visited = [False] * (v + 1)

def bfs():
    global queue, visited

    while queue:
        n = queue.popleft()
        print(n)
        for next_n in node[n]:
            if not visited[next_n]:
                visited[next_n] = True
                queue.append(next_n)

queue.append(1)
bfs()