for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 정답
    answer = 0

    def comparison_max(cnt):
        global answer

        if cnt != 1:
            answer = max(answer, cnt)

    # 가로 스캔
    for i in range(N):
        cnt = 0
        pre = 0
        for j in range(M):
            if lst[i][j] == 1:
                cnt += 1
                pre = 1
            elif lst[i][j] == 0 and pre == 1:
                comparison_max(cnt)
                cnt, pre = 0, 0
        comparison_max(cnt)

    # 세로 스캔
    for i in range(M):
        cnt = 0
        pre = 0
        for j in range(N):
            if lst[j][i] == 1:
                cnt += 1
                pre = 1
            elif lst[j][i] == 0 and pre == 1:
                comparison_max(cnt)
                cnt, pre = 0, 0
        comparison_max(cnt)

    print(f'#{tc} {answer}')
