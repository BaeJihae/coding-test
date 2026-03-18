# 방향 없는 그래프
import sys

readline = sys.stdin.readline
write = sys.stdout.write

N, E = map(int, readline().split()) # 노드의 개수, 엣지의 개수
node = []
for _ in range(N + 1):
    node.append([])

# 연결 요소
for _ in range(E):
    u, v = map(int, readline().split())
    node[u].append(v)
    node[v].append(u)

visited = [0] * (N + 1) # 방문 확인

def dfs(start):
    stack = [start]
    
    while stack:
        n = stack.pop()
        if not visited[n]:
            visited[n] = 1
            for new_n in node[n]:
                if not visited[new_n]:
                    stack.append(new_n)
    
    return

answer = 0 
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        answer += 1

write(str(answer))