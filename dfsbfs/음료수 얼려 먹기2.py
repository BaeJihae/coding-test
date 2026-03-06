# n, m 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 만들어지는 아이스크림의 개수
count = 0

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(graph, i, j): 
    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False
    if graph[i][j] == 0:
        graph[i][j] = True
        dfs(graph, i-1, j)
        dfs(graph, i, j-1)
        dfs(graph, i+1, j)
        dfs(graph, i, j+1)
        return True
    return False

# 모든 노드에 대해 음료수 채우기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            if dfs(graph, i, j) == 1:
                count += 1

print(count)