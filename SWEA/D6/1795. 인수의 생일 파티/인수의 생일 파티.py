from heapq import heappop, heappush


# adj : 인접리스트, n : 노드의 개수
def dijkstra(adj, n, s):
    # s -> x까지 노드의 최소 시간
    distance_lst = [float('inf')] * (n + 1)
    # 시작 노드와 끝 노드 초기화
    distance_lst[s] = 0

    min_heap = [(0, s)]  # (노드의 최소 거리, 시작 노드)

    # 시작 노드부터 각 노드까지의 최소 시간 구하기
    while min_heap:
        d, n = heappop(min_heap)
        for nxt_n, nxt_d in adj[n]:
            if distance_lst[nxt_n] > d + nxt_d:
                distance_lst[nxt_n] = d + nxt_d
                heappush(min_heap, (distance_lst[nxt_n], nxt_n))

    return distance_lst


def solution():
    for tc in range(1, int(input()) + 1):
        # n : 노드의 개수, m : 간선의 개수, s : 최종 노드
        n, m, s = map(int, input().split())

        # 인접 리스트 초기화
        adj = [[] * (n + 1) for _ in range(n + 1)]
        adj_op = [[] * (n + 1) for _ in range(n + 1)]

        for _ in range(m):
            # x : 출발 노드, y : 도착 노드, c : 거리
            x, y, c = map(int, input().strip().split())
            adj[x].append((y, c))     # 정상 방향으로의 인접 리스트 할당
            adj_op[y].append((x, c))  # 반대 방향의 인접 리스트 할당

        result_adj, result_adj_op = dijkstra(adj, n, s), dijkstra(adj_op, n, s)

        # 오고 가는데 걸리는 시간의 최댓값 구하기
        answer = 0
        for i in range(1, n + 1):
            answer = max(answer, result_adj[i] + result_adj_op[i])

        print(f'#{tc}', answer)


solution()
