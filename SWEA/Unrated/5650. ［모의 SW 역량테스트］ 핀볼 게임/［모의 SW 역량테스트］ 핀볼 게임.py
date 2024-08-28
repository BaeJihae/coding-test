# 핀볼게임

# 상하좌우로 이동하는 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 장애물 블록에 따른 방향 값
next_d = [
    [0],
    [1, 3, 0, 2],
    [3, 0, 1, 2],
    [2, 0, 3, 1],
    [1, 2, 3, 0],
    [1, 0, 3, 2]
]

for tc in range(1, int(input()) + 1):

    # 입력
    # 점수 판의 크기
    N = int(input())

    # 점수 판 저장
    game_board = [list(map(int, input().split())) for _ in range(N)]

    # 최대 점수
    max_score = 0

    # 웜홀 좌표값 저장
    warm_hole = {}

    # warm_hole 조사
    for i in range(N):
        for j in range(N):
            if game_board[i][j] in range(6, 11):
                # warm_hole 번호에 따른 2개의 좌표값 저장
                if game_board[i][j] in warm_hole:
                    warm_hole[game_board[i][j]] += [(i,j)]
                else:
                    warm_hole[game_board[i][j]] = [(i,j)]

    # 게임판 조사
    for i in range(N):
        for j in range(N):
            # 게임판이 0이라면 핀볼 게임 시작
            if game_board[i][j] == 0:
                # 현재 위치에서 상, 하, 좌, 우로 공 보내기
                for k in range(4):
                    c_i, c_j = i, j     # 현재 위치값 저장
                    cnt = 0             # 게임 점수 저장
                    direction = k       # 이동할 방향 저장
                    while True:
                        # 방향 이동
                        n_i = c_i + dx[direction]
                        n_j = c_j + dy[direction]

                        # 벽을 만날 경우
                        if n_i < 0 or n_i >= N or n_j < 0 or n_j >= N:
                            cnt += 1                            # 게임 점수 + 1
                            direction = next_d[5][direction]    # 벽에 부딪히는 건 5번인 네모박스에 부딪히는 것과 동일
                            c_i, c_j = n_i, n_j                 # 현재 위치 업데이트
                            continue

                        # 처음 위치에 도달하거나 블랙홀을 만난 경우
                        if (n_i == i and n_j == j) or game_board[n_i][n_j] == -1:
                            max_score = max(max_score, cnt)     # 게임 점수가 최댓값일 경우 업데이트
                            break                               # 반복문 종료

                        # 현재의 핀 위치 저장
                        pin_num = game_board[n_i][n_j]

                        # 장애물을 만난 경우
                        if pin_num in range(1, 6):
                            direction = next_d[pin_num][direction]  # 방향 업데이트
                            cnt += 1                                # 게임 점수 + 1
                        # 웜홀을 만난 경우
                        elif pin_num in range(6, 11):
                            for coordinate in warm_hole[pin_num]:
                                # 반대 웜홀 좌표값으로 현재 위치 증가
                                if (n_i, n_j) != coordinate:
                                    n_i, n_j = coordinate
                                    break

                        # 현재 위치 업데이트
                        c_i, c_j = n_i, n_j

    print(f'#{tc} {max_score}')