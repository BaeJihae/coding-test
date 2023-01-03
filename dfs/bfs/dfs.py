def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2, 3, 8]
    [1, 7]
    [1, 4, 5]
    [3, 5]
    [3, 4]
    [7]
    [2, 6, 8]
    [1, 7]
]

visited = [False]*9

# 그래프, 제일 처음 탐색할 노드, 방문처리할 리스트
dfs(graph, 1, visited)