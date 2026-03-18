import sys
from collections import deque
readline = sys.stdin.readline
write = sys.stdout.write

n, m, v = map(int, readline().split())
node = [[] for _ in range(n + 1)]

queue = deque()
visited_bfs = [False] * (n + 1)

def bfs():
    global queue, visited_bfs
    
    queue.append(v)
    visited_bfs[v] = True
    
    while queue:
        crt = queue.popleft()
        write(str(crt) + " ")
        for nxt in node[crt]:
            if not visited_bfs[nxt]:
                visited_bfs[nxt] = True
                queue.append(nxt)
    write('\n')


visited_dfs = [False] * (n + 1)

def dfs(v):
    if not visited_dfs[v]:
        write(str(v) + " ")
        visited_dfs[v] = True
        for nxt in node[v]:
            dfs(nxt)


for _ in range(m):
    i, j = map(int, readline().split())
    node[i].append(j)
    node[j].append(i)

for i in node:
    i.sort()

dfs(v)
print()
bfs()