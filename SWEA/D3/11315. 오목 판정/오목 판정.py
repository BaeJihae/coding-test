T = int(input())

# 우, 대각선 오아, 아, 대가선 왼아
di = [0, 1, 1, 1]
dj = [1, 1, 0, -1]


def omok(N, lst):
    for i in range(N - 4):
        for j in range(N):
            if lst[i][j] == 'o':
                for k in range(4):
                    count = 1
                    for z in range(1, 5):
                        ni = i + di[k] * z
                        nj = j + dj[k] * z

                        if ni < 0 or ni >= N or nj < 0 or nj >= N or lst[ni][nj] == '.':
                            break

                        count += 1
                    if count == 5:
                        return 'YES'

    for j in range(N - 4):
        for i in range(N - 3, N):
            if lst[i][j] == 'o':
                for k in range(4):
                    count = 1
                    for z in range(1, 5):
                        ni = i + di[k] * z
                        nj = j + dj[k] * z

                        if ni < 0 or ni >= N or nj < 0 or nj >= N or lst[ni][nj] == '.':
                            break

                        count += 1
                    if count == 5:
                        return 'YES'

    return 'NO'


for tc in range(1, T + 1):
    N = int(input())
    lst = [list(input()) for _ in range(N)]
    print(f'#{tc} {omok(N, lst)}')
