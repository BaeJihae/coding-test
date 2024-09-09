# 사방탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def shoot(idx, now_arr, now_blocks):
    global min_blocks

    if now_blocks == 0 or idx == N:
        min_blocks = min(min_blocks, now_blocks)
        return

    for col in range(W):
        copy_arr = [r[:] for r in now_arr]

        # 가장 위의 블럭 찾기
        row = -1
        for h in range(H):
            if copy_arr[h][col]:
                row = h
                break

        if row == -1:  # 벽돌이 없는 열이면 다음 열로 넘어가자
            continue

        # 깨뜨릴 벽돌 리스트
        lst = [(row, col, copy_arr[row][col])]
        copy_arr[row][col] = 0  # 벽돌 깨짐
        current_blocks = now_blocks - 1  # 남은 벽돌 수 - 1

        # 깨뜨릴 벽돌이 있을 때까지 반복
        while lst:
            r, c, p = lst.pop()
            for k in range(1, p):
                for i in range(4):
                    next_r = r + (dx[i] * k)
                    next_c = c + (dy[i] * k)

                    if next_r < 0 or next_r >= H or next_c < 0 or next_c >= W:  # 범위 확인
                        continue

                    if copy_arr[next_r][next_c] == 0:  # 깨질 벽돌이 없다면 넘어감
                        continue

                    lst.append((next_r, next_c, copy_arr[next_r][next_c]))
                    copy_arr[next_r][next_c] = 0  # 벽돌 깨짐
                    current_blocks -= 1  # 남은 벽돌 수 - 1

        # 벽돌 밑으로 떨어지기
        for cl in range(W):
            for rw in range(H - 1, -1, -1):
                if copy_arr[rw][cl] == 0:
                    for m in range(rw - 1, -1, -1):
                        if copy_arr[m][cl]:
                            copy_arr[m][cl], copy_arr[rw][cl] = copy_arr[rw][cl], copy_arr[m][cl]
                            break

        shoot(idx + 1, copy_arr, current_blocks)


for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    block_board = [list(map(int, input().split())) for _ in range(H)]

    min_blocks = 0  # 최소 블럭 개수
    # 현재 블럭 개수 조사
    for i in range(H):
        for j in range(W):
            if block_board[i][j]:
                min_blocks += 1

    shoot(0, block_board, min_blocks)

    print(f'#{tc} {min_blocks}')
