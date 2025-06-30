def cycle_graph(graph):
    visited = {}
    cycle_count = 0

    def dfs(n):
        visited[n] = 1

        for neighbor in graph.get(n, []):
            if visited.get(neighbor, 0) == 1:
                return True
            elif visited.get(neighbor, 0) == 0:
                if dfs(neighbor):
                    return True
        visited[n] = 2
        return False

    for node in graph.keys():
        if visited.get(node, 0) == 0:
            if dfs(node):
                cycle_count += 1

    return cycle_count

i = 0

while True:
    i += 1              # 케이스 번호
    n = int(input())    # 사람 명수

    if n == 0:          # 종료 조건
        break

    graph = {}

    # n번의 입력 받기
    for _ in range(n):
        toPerson, fromPerson = input().split()
        if toPerson not in graph:
            graph[toPerson] = []
        graph[toPerson].append(fromPerson)

    r = cycle_graph(graph)

    # 출력
    print(i, r)