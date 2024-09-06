# 우, 하, 좌, 상 좌표
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(row, col, depth, pre, visited, is_use_K):
    global answer

    for k in range(4):
        next_row, next_col = row + dx[k], col + dy[k]

        if next_row < 0 or next_row >= N or next_col < 0 or next_col >= N:
            continue

        if not visited[next_row][next_col]:
            if pre > lst[next_row][next_col]:
                visited[next_row][next_col] = True
                dfs(next_row, next_col, depth + 1, lst[next_row][next_col], visited, is_use_K)
                visited[next_row][next_col] = False
            else:
                if not is_use_K and lst[next_row][next_col] - K < pre:
                    visited[next_row][next_col] = True
                    dfs(next_row, next_col, depth + 1, pre - 1, visited, True)
                    visited[next_row][next_col] = False
    if answer < depth:
        answer = depth


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    highest_peak = max(max(row) for row in lst)  # 가장 높은 봉우리의 높이
    start_lst = []  # 가장 높은 봉우리 좌표 배열

    # 가장 높은 봉우리 찾기
    for row in range(N):
        for col in range(N):
            if lst[row][col] == highest_peak:
                start_lst.append((row, col))

    # 최대 길이
    answer = 0

    for x, y in start_lst:
        # K값 사용 여부 체크
        is_use_K = False

        # 방문 체크
        visited = [[False] * N for _ in range(N)]

        visited[x][y] = True
        dfs(x, y, 1, highest_peak, visited, is_use_K)

    print(f'#{tc}', answer)