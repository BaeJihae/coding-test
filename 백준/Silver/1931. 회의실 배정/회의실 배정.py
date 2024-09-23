import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
graph = [tuple(map(int, input().split())) for _ in range(n)]

graph.sort(key=lambda x: (x[1], x[0]))

cnt = 1
pre_end = graph[0][1]
for i in range(1, len(graph)):
    if pre_end <= graph[i][0]:
        cnt += 1
        pre_end = graph[i][1]

print(cnt)