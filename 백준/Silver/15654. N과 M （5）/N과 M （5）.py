n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

def permutation(m, visited, lst):

    if len(lst) == m:
        print(*lst)
        return

    for i in range(len(arr)):
        if not visited[i]:
            visited[i] = True
            permutation(m, visited, lst + [arr[i]])
            visited[i] = False

visited = [False] * n
permutation(m, visited, [])