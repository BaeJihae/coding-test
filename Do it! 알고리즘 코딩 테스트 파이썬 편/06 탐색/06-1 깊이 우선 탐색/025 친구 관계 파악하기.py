import sys

readline = sys.stdin.readline

v, e = map(int, readline().split())
node = [[] for _ in range(v)]
answer = 0
visited = [0] * (v)

for _ in range(e):
    a, b = map(int, readline().split())
    node[a].append(b)
    node[b].append(a)

def dfs(start, d):
    global answer
    
    if d == 5:
        answer = 1
        return
    
    visited[start] = 1
    for new_node in node[start]:
        if not visited[new_node]:
            dfs(new_node, d + 1)
    visited[start] = 0

for i in range(v):
    dfs(i, 1)
    
    if answer:
        break

print(answer)