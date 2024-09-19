import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

# 방향에 따른 이동 ( 동, 남, 서, 북 )
direction = ((0, 1), (1, 0), (0, -1), (-1, 0))

# 동 1 -> 0, 서 2 -> 2, 남 3 -> 1 북 4 -> 3
mapping_to_index = {1: 0, 2: 2, 3: 1, 4: 3}

# M: 세로 길이, N: 가로 길이
m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
start_x, start_y, start_d = map(int, input().split())  # 로봇의 출발지점과 방향
end_x, end_y, end_d = map(int, input().split())  # 로봇의 마지막지점과 방향


def bfs():
    queue = deque([(start_x - 1, start_y - 1, mapping_to_index[start_d], 0)])
    visited = [[[False] * n for _ in range(m)] for _ in range(4)]
    visited[mapping_to_index[start_d]][start_x - 1][start_y - 1] = True
    while queue:
        cx, cy, cd, k = queue.popleft()
        # 기저 조건
        if cx == end_x - 1 and cy == end_y - 1 and mapping_to_index[end_d] == cd:
            return k
        # 1 또는 2 또는 3칸 직진
        for d in range(1, 4):
            nx, ny = cx + direction[cd][0] * d, cy + direction[cd][1] * d
            # 벽을 만나면 더이상 직진 불가
            if nx < 0 or nx >= m or ny < 0 or ny >= n or board[nx][ny]:
                break
            if not visited[cd][nx][ny] and not board[nx][ny]:
                visited[cd][nx][ny] = True               # 방문표시
                queue.append((nx, ny, cd, k + 1))

        # 방향 바꾸기
        # 오른쪽 90도 회전
        if not visited[(cd + 1) % 4][cx][cy]:
            visited[(cd + 1) % 4][cx][cy] = True         # 방문표시
            queue.append((cx, cy, (cd + 1) % 4, k + 1))  
        # 왼쪽 90도 회전
        if not visited[(cd - 1) % 4][cx][cy]:
            visited[(cd - 1) % 4][cx][cy] = True         # 방문표시
            queue.append((cx, cy, (cd - 1) % 4, k + 1))

print(bfs())