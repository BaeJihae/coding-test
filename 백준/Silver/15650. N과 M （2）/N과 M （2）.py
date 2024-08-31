N, M = map(int, input().split())

def backtrack(idx, result):
    if len(result) == M:
        print(*result)
        return

    if idx == N:
        return

    backtrack(idx + 1, result + [idx + 1])
    backtrack(idx + 1, result)

backtrack(0, [])