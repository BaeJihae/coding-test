# 활주로 건설 여부 확인 함수
def is_build_runway(lst):
    # 경사로 설치 체크 리스트
    is_checked = [False] * N

    # 지형 탐색
    for i in range(0, N - 1):
        i, j = i, i + 1
        interval = abs(lst[i] - lst[j])  # 지형 높이 차이

        if interval >= 2:
            return False
        elif interval == 0:
            continue
        elif interval == 1:
            # 경사로가 증가
            if lst[i] < lst[j]:
                cnt = 0
                # 경사로를 설치할 수 있는지 확인
                for k in range(i - X + 1, i + 1):
                    if k >= 0 and lst[k] == lst[i] and not is_checked[k]:
                        cnt += 1
                    else:
                        return False
                # 경사로 설치 표시
                if cnt == X:
                    for z in range(i - X + 1, i + 1):
                        is_checked[z] = True
            # 경사로가 감소
            elif lst[i] > lst[j]:
                cnt = 0
                # 경사로를 설치할 수 있는지 확인
                for k in range(j, j + X):
                    if k < N and lst[k] == lst[j] and not is_checked[k]:
                        cnt += 1
                    else:
                        return False
                # 경사로 설치 표시
                if cnt == X:
                    for z in range(j, j + X):
                        is_checked[z] = True
    return True


for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    rand_board = [list(map(int, input().split())) for _ in range(N)]

    # 활주로 건설이 가능한 개수
    answer = 0

    # 가로 탐색
    for transverse_lst in rand_board:
        # 활주로 건설 여부 확인
        if is_build_runway(transverse_lst):
            answer += 1

    # 전치 행렬
    trans_rand_board = [list(row) for row in zip(*rand_board)]

    # 세로 탐색
    for transverse_lst in trans_rand_board:
        # 활주로 건설 여부 확인
        if is_build_runway(transverse_lst):
            answer += 1

    print(f'#{tc}', answer)
