# 최대 상금
def permutation(lst, idx):
    global answer, record_set

    if idx == C:
        current = int(''.join(map(str, lst)))
        if answer < current:
            answer = current
        return

    for i in range(0, N - 1):
        for j in range(i + 1, N):
            lst[i], lst[j] = lst[j], lst[i]
            num = ''.join(map(str, lst))
            if (idx, num) not in record_set:
                record_set.add((idx, num))
                permutation(lst, idx + 1)
            lst[i], lst[j] = lst[j], lst[i]


for tc in range(1, int(input()) + 1):
    # 입력
    num, C = map(int, input().split())
    list_N = list(map(int, list(str(num))))
    N = len(list_N)

    # 답
    answer = 0
    record_set = set()

    # 로직 수행
    permutation(list_N, 0)

    print(f'#{tc} {answer}')