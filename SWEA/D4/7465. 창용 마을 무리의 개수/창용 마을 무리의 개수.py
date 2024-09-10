def dfs(node):
    global visited

    for n in node_lst[node]:
        if not visited[n]:
            visited[n] = True
            dfs(n)
    else:
        return


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    node_lst = [[] for _ in range(N + 1)]

    for _ in range(M):
        node1, node2 = map(int, input().split())
        node_lst[node1].append(node2)
        node_lst[node2].append(node1)

    visited = [False] * (N + 1)
    answer = 0

    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            answer += 1

    print(f'#{tc} {answer}')