# 0: 1일, 1: 한 달, 2: 세 달
def dfs(fee, idx, visited):
    global answer

    # 기저조건 -> 12달을 체크 후의 요금 최저값 계산
    if idx >= 12:
        answer = min(fee, answer)
        return

    # 가지치기 -> 현재의 요금이 최저값보다 크다면 종료
    if fee > answer:
        return

    for k in range(3):
        # 요금 계산하지 않은 월
        if not visited[idx]:
            # 세 달 요금 계산
            if k == 2:

                for i in range(idx, idx + 3):
                    if i < 12:
                        visited[idx] = True

                dfs(fee + three_month_fee, idx + 3, visited)

                for i in range(idx, idx + 3):
                    if i < 12:
                        visited[idx] = False
            else:

                visited[idx] = True

                if k == 0:      # 1일 요금 계산
                    dfs(fee + lst[idx] * day_fee, idx + 1, visited)
                elif k == 1:    # 한 달 요금 계산
                    dfs(fee + month_fee, idx + 1, visited)

                visited[idx] = False
        # 요금 계산을 했거나 할 필요가 없는 월
        else:
            dfs(fee, idx + 1, visited)

for tc in range(1, int(input()) + 1):
    # 입력
    day_fee, month_fee, three_month_fee, year_fee = map(int, input().split())
    lst = list(map(int, input().split()))

    # 최저 수영장 요금
    answer = year_fee
    # 방문 노드
    visited = [False] * 12

    # 방문 체크
    for month in range(12):
        if lst[month] == 0:
            visited[month] = True

    dfs(0, 0, visited)

    # 출력
    print(f'#{tc} {answer}')
