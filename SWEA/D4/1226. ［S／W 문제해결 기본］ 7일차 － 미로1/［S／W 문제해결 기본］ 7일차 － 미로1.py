# import sys
# sys.stdin = open('input.txt')

N = 16
TC = 10


# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 시작점 찾기
def search_start():
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                return i, j


# 미로 찾기
def search_maze(c_i, c_j, visited):
    visited[c_i][c_j] = True

    if maze[c_i][c_j] == '3':
        return 1

    for k in range(4):
        n_i = c_i + dx[k]
        n_j = c_j + dy[k]

        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= N:
            continue

        if (maze[n_i][n_j] == '0' or maze[n_i][n_j] == '3') and not visited[n_i][n_j]:
            if search_maze(n_i, n_j, visited) == 1:
                return 1

    return 0


for _ in range(1, TC + 1):
    # 입력
    tc = int(input())
    maze = [list(input()) for _ in range(N)]

    # 방문 체크 리스트
    visited = [[False] * N for _ in range(N)]

    # 시작점
    s_i, s_j = search_start()
    visited[s_i][s_j] = True

    # 정답
    answer = search_maze(s_i, s_j, visited)
    print(f'#{tc} {answer}')
