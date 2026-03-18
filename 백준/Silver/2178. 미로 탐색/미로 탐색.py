import sys
from collections import deque
readline = sys.stdin.readline

n, m = map(int, readline().split())
board = [ list(readline())[0:m] for _ in range(n) ]
board = [[ int(k) for k in i] for i in board]
visited = [[False] * m for _ in range(n)]

def bfs():
    global board
    
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nxt_x, nxt_y = x + i, y + j
            if 0 <= nxt_x < n and 0 <= nxt_y < m and board[nxt_x][nxt_y] == 1 and not visited[nxt_x][nxt_y]:
                queue.append((nxt_x, nxt_y))
                visited[nxt_x][nxt_y] = True
                board[nxt_x][nxt_y] = board[x][y] + 1

bfs()
print(board[n - 1][m - 1])