# import sys
from copy import deepcopy
from collections import deque

# sys.stdin = open('input.txt')

# 상하좌우 탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 입력
N, M = map(int, input().split())
virus_board = [list(map(int, input().split())) for _ in range(N)]

# 비활성 바이러스
inactivity_virus = []

# 시간의 최솟값
answer = float('inf')

# 비활성 바이러스 조사
for i in range(N):
    for j in range(N):
        if virus_board[i][j] == 2:
            inactivity_virus.append((i, j))


# 조합 함수
def comb(idx, result):
    if len(result) == M:
        virus_infection(result)
        return

    if idx == len(inactivity_virus):
        return

    comb(idx + 1, result + [idx])
    comb(idx + 1, result)

def is_explore_next_virus(n_x, n_y, new_visited, new_virus_board):
    # 상하좌우 탐색
    for k_k in range(4):
        n_n_x, n_n_y = n_x + dx[k_k], n_y + dy[k_k]
        
        # 연구소 범위를 벗어나는 경우
        if 0 > n_n_x or n_n_x >= N or 0 > n_n_y or n_n_y >= N:
            continue
        
        # 빈칸이 있는 경우
        if not new_visited[n_n_x][n_n_y] and new_virus_board[n_n_x][n_n_y] == 0:
            return True
    
        # 아직 방문하지 않은 비활성 바이러스가 있는 경우 재귀적으로 탐색
        if not new_visited[n_n_x][n_n_y] and new_virus_board[n_n_x][n_n_y] == 2:
            new_visited[n_n_x][n_n_y] = True
            if is_explore_next_virus(n_n_x, n_n_y, new_visited, new_virus_board):
                return True
    
    # 주변에 빈칸이 없을 때 False 반환
    return False

# 바이러스 감염함수
def virus_infection(result):
    global answer

    activity_virus = deque()                    # 활성 바이러스
    new_virus_board = deepcopy(virus_board)     # 변경할 바이러스 보드
    visited = [[False] * N for _ in range(N)]   # 방문을 체크할 배열

    # 활성 상태로 만들 배열 번호 조사
    for i in result:
        x, y = inactivity_virus[i]
        visited[x][y] = True
        activity_virus.append((x, y))
        new_virus_board[x][y] = 0

    # 시간 체크
    time = 0

    while activity_virus:
        time += 1
        for _ in range(len(activity_virus)):
            c_x, c_y = activity_virus.popleft()

            # 상하좌우 탐색
            for k in range(4):
                n_x, n_y = c_x + dx[k], c_y + dy[k]

                # 연구소 범위를 벗어난 경우
                if 0 > n_x or n_x >= N or 0 > n_y or n_y >= N:
                    continue

                if not visited[n_x][n_y]:
                    visited[n_x][n_y] = True
                    # 빈칸인 경우
                    if new_virus_board[n_x][n_y] == 0:
                        new_virus_board[n_x][n_y] = time
                        activity_virus.append((n_x, n_y))
                    # 비활성 바이러스인 경우
                    elif new_virus_board[n_x][n_y] == 2:
                        new_visited = deepcopy(visited)
                        
                        # 다음 탐색을 해야하는지 확인
                        if is_explore_next_virus(n_x, n_y, new_visited, new_virus_board):
                            new_virus_board[n_x][n_y] = '*'
                            activity_virus.append((n_x, n_y))

    # 0인 값 찾기
    cnt = sum(row.count(0) for row in new_virus_board)

    # for arr in new_virus_board:
    #     print(*arr)
    # print()

    # 모든 영역에 바이러스가 전파되었는지 파악하기
    if cnt == M:
        answer = min(answer, time - 1)

# 함수 실행
comb(0, [])

# 출력
print(answer if answer != float('inf') else -1)
