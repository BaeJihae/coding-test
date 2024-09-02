from collections import deque

pipe_dict = {
    1: [1, 1, 1, 1],
    2: [1, 1, 0, 0],
    3: [0, 0, 1, 1],
    4: [1, 0, 0, 1],
    5: [0, 1, 0, 1],
    6: [0, 1, 1, 0],
    7: [1, 0, 1, 0]
}

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

checking_num = {0: 1, 1: 0, 2: 3, 3: 2}

def solution(start_x, start_y):
    global visited
    queue = deque([(1, start_x, start_y)])  # Start with idx=1, and initial position
    visited[start_x][start_y] = True

    while queue:
        idx, x, y = queue.popleft()

        if idx == L:
            continue

        for k in range(4):
            if pipe_dict[board[x][y]][k]:
                n_x = x + dx[k]
                n_y = y + dy[k]

                if 0 <= n_x < N and 0 <= n_y < M:
                    if board[n_x][n_y] != 0 and pipe_dict[board[n_x][n_y]][checking_num[k]] and not visited[n_x][n_y]:
                        visited[n_x][n_y] = True
                        queue.append((idx + 1, n_x, n_y))

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    solution(R, C)

    cnt = 0

    for i in range(N):
        for j in range(M):
            if visited[i][j]:
                cnt += 1

    print(f'#{tc}', cnt)
