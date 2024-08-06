T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = [list(map(int, list(input().strip()))) for _ in range(N)]
    answer = 0

    center = N // 2

    for i in range(center + 1):
        for j in range(center - i, center + i + 1):
            answer += lst[i][j]

    for i in range(center + 1, N):
        for j in range(i - center, N - (i - center)):
            answer += lst[i][j]

    print(f"#{tc} {answer}")