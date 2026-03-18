# 깊이 우선 탐색 
node = [[], [2, 3], [5, 6], [4], [6], [], []]

v = 6 # 노드의 개수
e = 6 # 에지의 개수

# 스택 버전
visited = [0] * (v + 1)
stack = []

def dfs(start):
    stack.append(start)
    
    while stack:
        x = stack.pop()
        
        if not visited[x]:
            visited[x] = 1
            
            for new_n in node[x]:
                if not visited[new_n]:
                    stack.append(new_n)

for i in range(1, v + 1):
    if not visited[i]:
        dfs(i)
        print(visited)

# 재귀함수 버전
visited = [False] * (v + 1)

def dfs2(v):
    if not visited[v]:
        visited[v] = True
        for n in node[v]:
            dfs2(n)

for i in range(1, v + 1):
    if not visited[i]:
        dfs2(i)
        print(visited)