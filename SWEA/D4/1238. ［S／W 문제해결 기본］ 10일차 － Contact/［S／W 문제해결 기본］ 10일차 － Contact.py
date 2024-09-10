import collections

def calculate_max(idx, node):
    global max_idx, answer_node

    if max_idx < idx:
        max_idx = idx
        answer_node = node
    elif max_idx == idx:
        if node > answer_node:
            answer_node = node


def bfs(idx, q):
    global max_idx, answer_node

    if not q:
        return

    for _ in range(len(q)):
        c_node = q.popleft()
        if c_node in node_lst.keys():
            N = len(node_lst[c_node])
            for n_node in node_lst[c_node]:
                if visited[n_node]:
                    N -= 1
                else:
                    visited[n_node] = True
                    q.append(n_node)
            if N == 0:
                calculate_max(idx, c_node)
        else:
            calculate_max(idx, c_node)

    bfs(idx + 1, q)




for tc in range(1, 11):
    N, first_node = map(int, input().split())
    lst = list(map(int, input().split()))

    node_lst = collections.defaultdict(list)
    visited = [False] * 101

    for i in range(0, N, 2):
        if lst[i + 1] not in node_lst[lst[i]]:
            node_lst[lst[i]].append(lst[i + 1])

    max_idx = 0
    answer_node = -1

    q = collections.deque()
    q.append(first_node)
    visited[first_node] = True

    bfs(1, q)

    print(f'#{tc}', answer_node)
