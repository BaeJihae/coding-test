from collections import deque

# 상하좌우에 따른 좌표 이동 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
M, N = map(int, input().split())
tomato_box = [list(map(int, input().split())) for _ in range(N)]

# 인지 않은 토마토의 개수
upripe_tomatoes = 0
# 조사할 토마토의 리스트
researched_tomatoes = deque()
# 일수
day = 0

# 박스 조사
for i in range(N):
    for j in range(M):
        # 토마토가 들어있지 않은 박스 세기
        if tomato_box[i][j] == 0:
            upripe_tomatoes += 1
        # 조사해야할 토마토 리스트
        elif tomato_box[i][j] == 1:
            researched_tomatoes.append([i, j])

# BFS 탐색
while researched_tomatoes:
    # 모든 토마토가 익은 경우 반복 종료
    if upripe_tomatoes == 0:
        break

    # 조사할 토마토의 개수만큼 반복
    for _ in range(len(researched_tomatoes)):

        # 조사할 개수
        i, j = researched_tomatoes.popleft()

        # 상하좌우 조사
        for k in range(4):
            # 상하좌우 이동
            n_i, n_j = i + dx[k], j + dy[k]
            # 좌표가 범위안이고, -1이 아니면
            if 0 <= n_i < N and 0 <= n_j < M and tomato_box[n_i][n_j] == 0:
                tomato_box[n_i][n_j] = 1
                researched_tomatoes.append([n_i, n_j])
                upripe_tomatoes -= 1
    # 일 수 증가
    day += 1

# 조사한 토마토의 개수와 토마토가 들어있지 않는 개수를 더한 것이 박스의 개수와 같다면
if upripe_tomatoes == 0:
    # 일 수 출력
    print(day)
# 아니라면
else:
    # -1 출력
    print(-1)
