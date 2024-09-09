from collections import deque

for tc in range(1, int(input()) + 1):
    N, M, K, A, B = map(int, input().split())
    lst_A = list(map(int, input().split()))   # 접수 창구의 번호당 처리 시간
    lst_B = list(map(int, input().split()))   # 정비 창구의 번호당 처리 시간
    customer_tk = list(map(int, input().split()))  # 고객의 도착 시간

    time = 0  # 시간
    completed_customer = 0       # 차량 정비를 완료한 고객
    waiting_repair = deque()     # 접수 창구를 기다리는 고객 번호
    waiting_reception = deque()  # 정비 창구를 기다리는 고객 번호
    lst_repair = [None] * N      # 현재 접수 창구의 상태
    lst_reception = [None] * M   # 현재 정비 창구의 상태
    search_A, search_B = [], []  # 찾고자 하는 접수/정비 창고의 고객 번호

    # 고객의 대기번호를 딕셔너리에 정리
    tk_dict = {}
    for idx, tk in enumerate(customer_tk):
        if tk in tk_dict:
            tk_dict[tk].append(idx)
        else:
            tk_dict[tk] = [idx]

    while True:
        # 모든 고객이 차량 정비를 완료했다면 종료
        if completed_customer == K:
            break

        # 도착한 손님 접수 대기줄에 넣기
        if time in tk_dict:
            waiting_repair.extend(tk_dict[time])

        waiting_tmp = []
        # 접수 창고를 기다리는 사람이 있거나 접수 창고안에 손님이 있다면
        if waiting_repair or lst_repair.count(None) != N:
            for n in range(N):
                if lst_repair[n]: # 접수 창고가 비어있지 않은 경우
                    if lst_repair[n][1] == lst_A[n]: # 접수가 끝났다면
                        waiting_tmp.append((n,lst_repair[n][0]))  # 정비 창구 대기줄로 보내기
                        lst_repair[n] = None # 접수 창고 비우기
                    else: # 접수가 끝나지 않았다면
                        lst_repair[n][1] += 1 # 접수 시간 + 1
                if not lst_repair[n] and waiting_repair: # 접수 창구가 비어있고, 대기 손님이 있을 경우
                    customer_number = waiting_repair.popleft()
                    lst_repair[n] = [customer_number, 1]  # 정비 창구에 대기 손님 보내기
                    # 찾고자 하는 A 창구라면 고객 번호 저장
                    if n == A - 1:
                        search_A.append(customer_number + 1)
        waiting_tmp.sort(key=lambda x: x[0])
        waiting_reception.extend(map(lambda x: x[1], waiting_tmp))

        # 정비 창구를 기다리는 사람이 있거나 정비 창구안에 손님이 있다면
        if waiting_reception or lst_reception.count(None) != M:
            for m in range(M):
                if lst_reception[m]: # 정비 창고가 비어있지 않은 경우
                    if lst_reception[m][1] == lst_B[m]: # 정비가 끝났다면
                        lst_reception[m] = None # 정비 창고 비우기
                    else: # 정비가 끝나지 않았다면
                        lst_reception[m][1] += 1 # 정비 시간 + 1
                if not lst_reception[m] and waiting_reception: # 정비 창구가 비어있고, 대기 손님이 있을 경우
                    customer_number = waiting_reception.popleft()
                    lst_reception[m] = [customer_number, 1]  # 정비 창구에 대기 손님 보내기
                    completed_customer += 1 # 완료된 고객 + 1
                    # 찾고자 하는 B 창구라면 고객 번호 저장
                    if m == B - 1:
                        search_B.append(customer_number + 1)

        # 시간 증가
        time += 1

    inter_set = set(search_A) & set(search_B)
    if inter_set:
        answer = sum(inter_set)
    else:
        answer = -1

    print(f'#{tc}', answer)