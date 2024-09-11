import sys
from heapq import heappush, heappop

input = sys.stdin.readline

# adj : 인접 리스트, s : 시작 정점, V : 정점 개수
def dijkstra(adj, s, V):
    # 방문 체크 ( 사이클 방지 )
    visited = [False] * (V + 1)

    # 최소 힙
    min_heap = [(0, s)]  # (노드, 가중치)

    # 가중치를 입력할 리스트
    distance_lst = [float('inf')] * (V + 1)
    distance_lst[s] = 0  # 시작점 초기화

    while min_heap:
        weight, node = heappop(min_heap)  # 노드와 가중치
        if not visited[node]:  # 탐색할 노드 방문 체크
            visited[node] = True  # 방문 표시
            for nxt_node, nxt_weight in adj[node]:
                if not visited[nxt_node]:  # 다음 노드 방문 체크
                    # 원래 가지고 있던 가중치값과 그 전 가중치와 현재 가중치을 합친 가중치 비교
                    if distance_lst[nxt_node] > weight + nxt_weight:
                        distance_lst[nxt_node] = weight + nxt_weight
                        heappush(min_heap, (distance_lst[nxt_node], nxt_node))
    return distance_lst


def solution():
    V, E = map(int, input().split())
    K = int(input())

    # 인접 리스트 초기화
    adj = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        adj[u].append((v, w))
        
    # 최단 경로의 경로값
    distance_lst = dijkstra(adj, K, V)

    # 최단 경로의 경로값 출력
    [print('INF' if distance_lst[i] == float('inf') else distance_lst[i]) for i in range(1, V + 1)]


solution()
