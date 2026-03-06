# 이차원 리스트를 이용한 그래프 추천
import sys
input = sys.stdin.readline


# 입력값
# 3 4
# 1 2 4
# 1 3 7
# 2 1 10
# 3 2 6

N, E = map(int, input().split())

# 이차원 리스트 선언과 초기화
graph = [[] for _ in range(N+1)]

for i in range(E):
    n1, n2, e = map(int, input().split())
    graph[n1].append((n2, e))

for g in graph:
    for nextNode, weight in g:
        print(f'{g}다음노드는 {nextNode}이고, 거리는 {weight}입니다.')  