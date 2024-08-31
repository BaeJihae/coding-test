N, M = map(int, input().split())

def backtrack(idx, result):
    if len(result) == M:
        print(*result)
        return

    for i in range(N):
        backtrack(idx + 1, result + [i + 1])

backtrack(0, [])