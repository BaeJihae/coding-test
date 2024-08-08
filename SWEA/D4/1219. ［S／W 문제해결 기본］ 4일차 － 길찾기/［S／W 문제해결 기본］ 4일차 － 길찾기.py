# 길찾기
for _ in range(10):
    tc, N = map(int, input().split())
    mp = list(map(int, input().split()))

    size = [[] for _ in range(100)]
    visited = [False]*100

    for i in range(0, N*2, 2):
        size[mp[i]].append(mp[i+1])

    def dfs(v):
        visited[v] = True
        stack = []

        while True:
            for w in size[v]:
                if w == 99:
                    return 1
                if not visited[w]:
                    stack.append(v)
                    v = w
                    visited[w] = True
                    break
            else:
                if stack:
                    v = stack.pop()
                else:
                    break
        return 0

    print(f'#{tc} {dfs(0)}')