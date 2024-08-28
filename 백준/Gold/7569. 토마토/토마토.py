from collections import deque

# 상하좌우위아래에 따른 좌표 이동 값
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

# 입력
M, N, H = map(int, input().split())
tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 익지 않은 토마토의 개수
upripe_tomatoes = 0
# 조사할 토마토의 리스트
researched_tomatoes = deque()

# 박스 조사
for h in range(H):
    for i in range(N):
        for j in range(M):
            # 익지 않은 토마토 세기
            if tomato_box[h][i][j] == 0:
                upripe_tomatoes += 1
            # 익은 토마토 위치 저장
            elif tomato_box[h][i][j] == 1:
                researched_tomatoes.append([h, i, j])

# BFS 탐색
day = 0
while researched_tomatoes:
    # 모든 토마토가 익은 경우 반복 종료
    if upripe_tomatoes == 0:
        break

    # 조사할 토마토의 개수만큼 반복
    for _ in range(len(researched_tomatoes)):
        # 조사할 토마토 좌표
        h, i, j = researched_tomatoes.popleft()

        # 상하좌우위아래 조사
        for direction in range(6):
            # 상하좌우위아래 이동
            n_h, n_i, n_j = h + dz[direction], i + dx[direction], j + dy[direction]
            # 좌표가 범위 안이고, 토마토가 익지 않은 경우
            if 0 <= n_h < H and 0 <= n_i < N and 0 <= n_j < M and tomato_box[n_h][n_i][n_j] == 0:
                tomato_box[n_h][n_i][n_j] = 1  # 토마토를 익게 만들기
                researched_tomatoes.append([n_h, n_i, n_j])  # 익은 토마토 큐에 추가
                upripe_tomatoes -= 1  # 익지 않은 토마토 개수 감소
    # 일 수 증가
    day += 1

# 모든 토마토가 익었다면
if upripe_tomatoes == 0:
    print(day)
# 일부 토마토가 익지 못한 경우
else:
    print(-1)
