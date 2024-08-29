# 연구소
from collections import deque
import copy

# 입력
N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우에 따른 좌표 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 빈칸인 좌표를 저장할 배열
blank_arr = []
# 바이러스가 들어있는 좌표를 저장할 배열
virus_arr = []
# 안전 영역 크기의 최댓값
answer = 0

# 좌표 탐색
for i in range(N):
    for j in range(M):
        if lst[i][j] == 0:
            blank_arr.append((i, j))
        elif lst[i][j] == 2:
            virus_arr.append((i, j))


# 조합 함수
def comb(i, result, n):
    if len(result) == 3:
        viral_transmission(result, lst)
        return

    if i == n:
        return

    comb(i + 1, result + [blank_arr[i]], n)
    comb(i + 1, result, n)


# 바이러스 퍼트려서 빈칸 개수 찾기
def viral_transmission(coordinate_arr, board):
    global answer
    
    new_board = copy.deepcopy(board)
    virus_queue = deque(virus_arr)
    
    # 벽 세우기
    for i, j in coordinate_arr:
        new_board[i][j] = 1

    # 벽 세운 후 바이러스 전염
    while virus_queue:
        c_i, c_j = virus_queue.popleft()

        for k in range(4):
            n_i, n_j = c_i + dx[k], c_j + dy[k]
            
            # 좌표 범위 넘어가면 넘어가기
            if n_i < 0 or n_i >= N or n_j < 0 or n_j >= M:
                continue
            
            # 빈칸이라면 바이러스 전염시키고, 탐색할 배열에 추가
            if new_board[n_i][n_j] == 0:
                new_board[n_i][n_j] = 2
                virus_queue.append((n_i, n_j))
    
    # 빈칸 개수 조사
    cnt = sum(row.count(0) for row in new_board)
    # 최댓값 저장
    answer = max(answer, cnt)


# 함수 실행
comb(0, [], len(blank_arr))
print(answer)
