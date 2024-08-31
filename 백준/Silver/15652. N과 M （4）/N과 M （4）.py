N, M = map(int, input().split())

def backtrack(idx, result):
    if len(result) == M:
        print(*result)
        return

    if not result:
        start = 0
    else:
        start = result[-1] - 1

    for i in range(start, N):
        backtrack(idx + 1, result + [i + 1])

backtrack(0, [])