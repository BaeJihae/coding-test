import sys
from collections import deque
readline = sys.stdin.readline

N = int(readline()) # N 노드의 개수 입력받기

# node 노드 리스트에 (노드 번호, 가중치) 저장
node = [[] for _ in range(N + 1)]
for _ in range(N):
    lst = list(map(int, readline().split()))
    i, lst = lst[0], lst[1:-1]
    for k in range(0, len(lst), 2):
        node[i].append((lst[k], lst[k + 1]))

visited = [False] * (N + 1) # visited 방문한 노드 체크
distance = [0] * (N + 1)    # 가중치 저장할 배열

# bfs
def bfs(start_n):
    queue = deque()
    # 임의의 노드값 가져와서 큐에 저장
    queue.append(start_n)
    visited[start_n] = True
    
    while queue:
        n = queue.popleft()
        for nxt_n, nxt_d in node[n]:
            if not visited[nxt_n]:
                # 큐에 저장된 노드값을 꺼내서 가중치 값 계산
                queue.append((nxt_n))
                distance[nxt_n] = nxt_d + distance[n]
                visited[nxt_n] = True

# 임의의 노드 1을 골라서 bfs를 실행하며 최고의 길이 노드 찾기
bfs(1)
mx, start_node = 0, 0
for i, k in enumerate(distance):
    if mx < k:
        mx = k
        start_node = i

# 최고의 길이 노드에서 시작해 bfs를 실행하여 가장 긴 지름 찾기
# 가중치 저장할 배열 초기화
visited = [False] * (N + 1)
distance = [0] * (N + 1)

bfs(start_node)
print(max(distance))