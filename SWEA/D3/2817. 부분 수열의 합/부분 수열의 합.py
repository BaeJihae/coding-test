def sub_set(sum, idx):
    global answer

    if idx == N:
        if sum == K:
            answer += 1
        return

    sub_set(sum + lst[idx], idx + 1)
    sub_set(sum, idx + 1)


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    lst = list(map(int, input().split()))

    # 부분 수열의 합이 K인 수열의 개수
    answer = 0
    sub_set(0, 0)
    print(f'#{tc}', answer)