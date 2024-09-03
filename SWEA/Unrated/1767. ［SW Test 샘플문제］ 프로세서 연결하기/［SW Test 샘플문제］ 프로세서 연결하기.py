from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def solution(i, lst, wire_sum, process_cnt):
    global min_wire_length, max_process_cnt

    # 종료조건
    if i == len(q):
        if max_process_cnt < process_cnt:
            min_wire_length, max_process_cnt = wire_sum, process_cnt
        elif max_process_cnt == process_cnt:
            if min_wire_length > wire_sum:
                min_wire_length, max_process_cnt = wire_sum, process_cnt
        return

    x, y = q[i]
    for k in range(4):
        n_x, n_y = x, y
        new_lst = [row[:] for row in lst]
        cnt = 0
        while True:
            n_x += dx[k]
            n_y += dy[k]

            if n_x < 0 or n_x >= N or n_y < 0 or n_y >= N:
                solution(i + 1, new_lst, wire_sum + cnt, process_cnt + 1)
                break
            if new_lst[n_x][n_y] != 0:
                break
            else:
                new_lst[n_x][n_y] = 3
                cnt += 1
    new_lst = [row[:] for row in lst]
    solution(i + 1, new_lst, wire_sum, process_cnt)


for tc in range(1, int(input()) + 1):
    # 입력
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 정답
    min_wire_length, max_process_cnt = float('inf'), 0

    q = deque()
    process_num = len(q)
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            if lst[i][j] == 1:
                q.append((i, j))

    solution(0, lst, 0, 0)

    if min_wire_length == float('inf'):
        min_wire_length = 0

    print(f'#{tc}', min_wire_length)
