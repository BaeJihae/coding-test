# 오셀로 게임
T = int(input())

di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]

for tc in range(1, T+1):
    N, M = map(int, input().split())

    lst = [[0]*N for _ in range(N)]
    lst[N // 2 - 1][N // 2 - 1] = lst[N // 2][N // 2] = 2
    lst[N // 2][N // 2 - 1] = lst[N // 2 - 1][N // 2] = 1

    # 돌 하나 놓을 때의 보드 변환
    def place_piece(i, j, p):
        global lst
        lst[i][j] = p

        for k in range(8):
            pre_i, pre_j = i, j
            ij_lst = []
            for cn in range(1, N):
                next_i = pre_i + di[k] * cn
                next_j = pre_j + dj[k] * cn
                if 0 <= next_i < N and 0 <= next_j < N and lst[next_i][next_j] != 0:
                    if lst[next_i][next_j] == p:
                        for pos in ij_lst:
                            lst[pos[0]][pos[1]] = p
                        break
                    else:
                        ij_lst.append([next_i, next_j])
                else:
                    break

    # 2차원 배열의 흑, 돌 개수 세기
    def cnt_BW():
        global lst
        cnt_B, cnt_W = 0, 0

        for l in lst:
            cnt_B += l.count(1)
            cnt_W += l.count(2)

        return cnt_B, cnt_W

    # 흑돌, 백돌 놓기
    for _ in range(M):
        i, j, p = map(int, input().split())
        place_piece(j-1, i-1, p)

    cnt_B, cnt_W = cnt_BW()
    print(f'#{tc} {cnt_B} {cnt_W}')