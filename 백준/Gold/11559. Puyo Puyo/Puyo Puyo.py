import sys
from collections import deque

input = lambda: sys.stdin.readline().strip()

# 상수
W, H = 6, 12
# 상대방의 필드 정보 받기
field = [list(input()) for _ in range(12)]


def bfs(visited, x, y):
    queue = deque([(x, y)])
    lst = [(x, y)]
    visited[x][y] = True
    cnt = 1
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = cx + dx, cy + dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if field[nx][ny] == field[cx][cy] and not visited[nx][ny]:
                visited[nx][ny] = True
                cnt += 1
                queue.append((nx, ny))
                lst.append((nx, ny))
    if cnt >= 4:
        return lst
    else:
        return


def solution(field):
    answer = 0

    while True:
        visited = [[False] * W for _ in range(H)]
        puyo_lst = []
        for i in range(H - 1, -1, -1):
            for j in range(W):
                if field[i][j] != '.':
                    arr = bfs(visited, i, j)
                    if arr:
                        puyo_lst.extend(arr)
        if not puyo_lst:
            break
        else:
            # 없어져야하는 puyo 지우기
            for x, y in puyo_lst:
                field[x][y] = '.'
            # 남아있는 뿌요 밑으로 떨어뜨리기
            for w in range(W):
                for h in range(H - 1, -1, -1):
                    if field[h][w] == '.':
                        for k in range(h - 1, -1, -1):
                            if field[k][w] != '.':
                                field[h][w], field[k][w] = field[k][w], field[h][w]
                                break
        answer += 1
        # for row in field:
        #     print(*row)
        # print()
    return answer


print(solution(field))