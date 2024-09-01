from collections import deque

def search_parent(N, tree_dict):
    q = deque([1])
    parent = [0] * (N+1)
    while q:
        curent_node = q.popleft()
        for i in tree_dict[curent_node]:
            if parent[i] == 0 and i != 1:
                parent[i] = curent_node
                q.append(i)
    return parent

N = int(input())
tree_dict = {}
for _ in range(N - 1):
    node1, node2 = map(int, input().split())
    if node1 in tree_dict:
        tree_dict[node1].append(node2)
    else:
        tree_dict[node1] = [node2]

    if node2 in tree_dict:
        tree_dict[node2].append(node1)
    else:
        tree_dict[node2] = [node1]

result = search_parent(N, tree_dict)
for i in range(2, N+1):
    print(result[i])
