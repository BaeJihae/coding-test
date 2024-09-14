# 말이 되고픈 원숭이
import sys
from collections import deque
input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, -1, 1, -1, 1, -1, 0, 0]
dy = [1, -1, -1, 1, 2, 2, -2, -2, 0, 0, 1, -1]

def bfs(move_board, K):
    move_cnt = float('inf')
    q = deque([(0, 0, 0, K)])  # (x좌표, y좌표, 거리)로 q 초기화

    # 3중 방문 체크
    visited = [[[False] * (K + 1) for _ in range(W)] for _ in range(H)]
    visited[0][0][K] = True

    while q:
        x, y, dist, k = q.popleft()

        # 기저 조건
        if x == H - 1 and y == W - 1:
            return dist

        for d in range(12):
            # 다음 이동 거리
            nxt_x, nxt_y = x + dx[d], y + dy[d]

            # 범위를 벗어나거나 장애물이 있거나 방문했다면 종료
            if nxt_x < 0 or nxt_x >= H or nxt_y < 0 or nxt_y >= W or move_board[nxt_x][nxt_y] == 1:
                continue

            # 말로 이동 할 경우 말로 움직일 수 있는 횟수 - 1
            if d in range(0, 8) and k > 0 and not visited[nxt_x][nxt_y][k - 1]:
                visited[nxt_x][nxt_y][k - 1] = True
                q.append((nxt_x, nxt_y, dist + 1, k - 1))
            elif d in range(8, 12) and not visited[nxt_x][nxt_y][k]:
                visited[nxt_x][nxt_y][k] = True
                q.append((nxt_x, nxt_y, dist + 1, k))

    return -1


K = int(input())  # 말처럼 움직일 수 있는 횟수
W, H = map(int, input().split())  # W:가로길이, H:세로길이
move_board = [list(map(int, input().split())) for _ in range(H)]

# 원숭이의 동작 수
min_move_cnt = bfs(move_board, K)
print(min_move_cnt)
