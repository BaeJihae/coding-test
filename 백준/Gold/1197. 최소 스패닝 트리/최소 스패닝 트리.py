import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
V, E = map(int, input().split())
graph = []

# 입력
for _ in range(E):
    A, B, C = map(int, input().split())
    if A > B:
        A, B = B, A
    graph.append((C, A, B))

# 간선 길이 짧은 순서대로 정렬
graph.sort(key=lambda x: x[0])

parents = [i for i in range(V + 1)]

def find(v):
    if parents[v] != v:
        parents[v] = find(parents[v])

    return parents[v]

def union(u, v):
    u = find(u)
    v = find(v)

    parents[v] = u

    if u == v:
        return False
    else:
        return True

answer = 0
for l, u, v in graph:
    if union(u, v):
        answer += l

print(answer)