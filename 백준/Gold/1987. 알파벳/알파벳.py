import sys
input = lambda: sys.stdin.readline().rstrip()

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(row, column, x, y, visited, cnt, board, alphabet_lst):
    global max_move_cnt

    is_not_move = 0

    for k in range(4):
        nxt_x, nxt_y = x + dx[k], y + dy[k]

        if nxt_x < 0 or nxt_x >= row or nxt_y < 0 or nxt_y >= column or visited[nxt_x][nxt_y]\
                or alphabet_lst[ord(board[nxt_x][nxt_y]) - ord('A')]:
            is_not_move += 1
            continue

        visited[nxt_x][nxt_y] = 1
        alphabet_lst[ord(board[nxt_x][nxt_y]) - ord('A')] = True
        bfs(row, column, nxt_x, nxt_y, visited, cnt + 1, board, alphabet_lst)
        visited[nxt_x][nxt_y] = 0
        alphabet_lst[ord(board[nxt_x][nxt_y]) - ord('A')] = False

    if is_not_move == 4 and cnt > max_move_cnt:
        max_move_cnt = cnt
        return


def solution():
    row, column = map(int, input().split())
    board = [list(input()) for _ in range(row)]

    visited = [[0] * column for _ in range(row)]
    visited[0][0] = 1
    alphabet_lst = [False] * 26
    alphabet_lst[ord(board[0][0]) - ord('A')] = True
    bfs(row, column, 0, 0, visited, 1, board, alphabet_lst)


max_move_cnt = 0
solution()
print(max_move_cnt)
