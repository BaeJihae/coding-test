R, C = map(int, input().split())
map_data = [list(input()) for _ in range(R)]

answer = 0

def dfs(i, j):
    if j == C - 1:
        return True
    for di in [-1, 0, 1]:  # 위, 중간, 아래 순서
        ni, nj = i + di, j + 1
        if 0 <= ni < R and 0 <= nj < C and map_data[ni][nj] == '.':
            map_data[ni][nj] = '#'
            if dfs(ni, nj):
                return True
    return False

for i in range(R):
    map_data[i][0] = '#'
    if map_data[i][1] == '.':
        map_data[i][1] = '#'
        if dfs(i, 1):
            answer += 1

print(answer)