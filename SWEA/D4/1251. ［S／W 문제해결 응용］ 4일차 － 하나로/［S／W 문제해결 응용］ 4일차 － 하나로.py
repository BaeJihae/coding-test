from heapq import heappop, heappush
from math import sqrt


# s:임의의 시작 섬, N:섬의 개수, lst_x:x좌표 리스트, lst_y:y좌표 리스트
def prim(s, N, lst_x, lst_y):
    visited = [False] * N  # 방문 체크 노드
    min_heap = [(0, s)]    # (섬까지의 최소 길이, 섬의 번호)를 담고 있는 최소 힙

    mst = [] # 각 섬끼리의 최솟값 거리를 가진 배열

    while min_heap:
        # distance : 이전 섬에서 현재 섬까지의 최소 거리, 섬 
        distance, node = heappop(min_heap)
        if not visited[node]:       # 방문 체크
            visited[node] = True 
            mst.append(distance)    # 현재 섬가지의 최소 거리 저장
            for i in range(N):      # 모든 섬을 체크하며
                if not visited[i]:  # 방문 여부를 확인하고
                    # 이전 섬과 방문하지 않은 나머지 섬까지의 거리계산
                    current_distance = sqrt((lst_x[node] - lst_x[i]) ** 2 + (lst_y[node] - lst_y[i]) ** 2)
                    heappush(min_heap, (current_distance, i))

    return mst


def solution():
    for tc in range(1, int(input()) + 1):
        N = int(input()) # 섬들의 개수
        lst_x = list(map(int, input().split())) # 섬들의 x 좌표 값
        lst_y = list(map(int, input().split())) # 섬들의 y 좌표 값
        E = float(input()) # 환경 부담 세율
    
        MST = prim(0, N, lst_x, lst_y) 
        
        # 환경 부담금 계산
        answer = 0.0
        for k in range(1, N):
            answer += E * MST[k] ** 2

        print(f'#{tc}', round(answer))


solution()
