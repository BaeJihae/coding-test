from collections import deque

# n, m 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 만들어지는 아이스크림의 개수
count = 0

# BFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def bfs(graph, i, j): 
    queue = deque([(i,j)])
    graph[i][j] = 1
    while queue:
        (x, y) = queue.popleft()
        if 0 < y+1 < m :
            if graph[x][y+1] == 0:
                queue.append((x, y+1))
                graph[x][y+1] = 1
        if 0 < x+1 < n :
            if graph[x+1][y] == 0:
                queue.append((x+1, y))
                graph[x+1][y] = 1
        if 0 <= y-1 < m-1 :
            if graph[x][y-1] == 0:
                queue.append((x, y-1))
                graph[x][y-1] = 1
        if 0 <= x-1 < n-1 :
            if graph[x-1][y] == 0:
                queue.append((x-1, y))
                graph[x-1][y] = 1
    return 1

# 모든 노드에 대해 음료수 채우기
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            if bfs(graph, i, j) == 1:
                count += 1

print(count)