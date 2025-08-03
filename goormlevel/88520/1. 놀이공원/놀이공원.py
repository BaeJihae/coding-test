import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    
    answer = K * K 

    for i in range(N - K + 1):
        window_sum = []
        for j in range(N):
            col_sum = sum(board[i + r][j] for r in range(K))
            window_sum.append(col_sum)

        curr = sum(window_sum[:K])
        answer = min(answer, curr)

        for y in range(1, N - K + 1):
            curr += window_sum[y + K - 1] - window_sum[y - 1]
            answer = min(answer, curr)

    print(answer)
