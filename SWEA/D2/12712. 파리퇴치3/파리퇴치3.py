# 파리퇴치3
T = int(input())

di = [[1, 0, -1, 0],[1, 1, -1, -1]]
dj = [[0, 1, 0, -1],[1, -1, 1, -1]]

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = [ list(map(int, input().split())) for _ in range(N) ]
    answer = -1
    for i in range(N):
        for j in range(N):
            for k in range(2):
                sm = lst[i][j]
                for l in range(4):
                    for m in range(1, M):
                        ci = i + di[k][l] * m
                        cj = j + dj[k][l] * m
                        if 0 <= ci < N and 0 <= cj < N:
                            sm += lst[ci][cj]
                if answer < sm:
                    answer = sm
    
    print(f'#{tc} {answer}')
