import sys
input = lambda: sys.stdin.readline().rstrip()


def floyd_warshall(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] >= 2:
                    graph[i][j] = 1

    for row in graph:
        print(*row)
    return


# 입력
n = int(input())  # n: 정점의 개수
graph = [list(map(int, input().split())) for _ in range(n)]  # 인접행렬

floyd_warshall(n, graph)