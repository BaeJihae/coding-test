# 연구소
from collections import deque
import copy

# 입력
N, M = map(int, input().split())
virus_board = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우에 따른 좌표 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 바이러스를 놓을 수 있는 칸
possible_virus = []
# 바이러스를 퍼뜨리는 최소 시간 ( 정답 )
answer = float('inf')

# 좌표 탐색
for i in range(N):
    for j in range(N):
        if virus_board[i][j] == 2:
            possible_virus.append((i, j))


# 조합 함수
def comb(i, result): # i는 탐색 깊이, result는 조합의 결과
    if len(result) == M:
        viral_transmission(result, virus_board)
        return

    if i == len(possible_virus):
        return

    comb(i + 1, result + [possible_virus[i]])
    comb(i + 1, result)


# 바이러스 퍼트려서 빈칸 개수 찾기
def viral_transmission(arr, virus_board):
    global answer

    new_virus_board = copy.deepcopy(virus_board)
    virus_queue = deque(arr)

    visited = [[False] * N for _ in range(N)]
    time = 0

    for i, j in virus_queue:
        new_virus_board[i][j] = 0
        visited[i][j] = True

    # 바이러스 전염
    while virus_queue:
        time += 1
        for _ in range(len(virus_queue)):
            c_i, c_j = virus_queue.popleft()

            for k in range(4):
                n_i, n_j = c_i + dx[k], c_j + dy[k]

                # 좌표 범위 넘어가면 넘어가기
                if n_i < 0 or n_i >= N or n_j < 0 or n_j >= N:
                    continue

                # 바이러스 감염시키기
                if ( new_virus_board[n_i][n_j] == 0 or new_virus_board[n_i][n_j] == 2 ) and not visited[n_i][n_j]:
                    new_virus_board[n_i][n_j] = 9
                    virus_queue.append((n_i, n_j))
                elif new_virus_board[n_i][n_j] == 1 and not visited[n_i][n_j]:
                    new_virus_board[n_i][n_j] = '-'

                visited[n_i][n_j] = True

    cnt = 0
    for x in range(N):
        for y in range(N):
            if new_virus_board[x][y] == 0 or new_virus_board[x][y] == 2:
                cnt += 1

    if cnt == M:
        answer = min(time - 1, answer)

# 함수 실행
comb(0, [])

if answer == float('inf'):
    print(-1)
else:
    print(answer)