def calculate_taste(lst_A):
    lst_B = []
    for i in range(N):
        if i not in lst_A:
            lst_B.append(i)

    A, B = 0, 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            A += (lst[lst_A[i]][lst_A[j]] + lst[lst_A[j]][lst_A[i]])
            B += (lst[lst_B[i]][lst_B[j]] + lst[lst_B[j]][lst_B[i]])
    return abs(A - B)


def comb(idx, result):
    global answer, cnt

    if len(result) == N // 2:
        cnt += 1
        taste_difference = calculate_taste(result)
        if answer > taste_difference:
            answer = taste_difference
        return

    if idx >= N:
        return

    comb(idx + 1, result + [idx])
    comb(idx + 1, result)


for tc in range(1, int(input()) + 1):
    # 입력
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 정답
    answer = float('inf')
    cnt = 0
    comb(1, [0])

    # 출력
    print(f'#{tc}', answer)