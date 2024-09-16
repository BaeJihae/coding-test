import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# 사방 탐색을 위한 좌표 이동
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


# mp: 고슴도치가 이동하는 맵, time: 이동 시간
# cnt_x: 현재 고슴도치의 행 위치, cnt_y: 현재 고슴도치의 열 위치, water_lst: 물의 위치
def bfs(mp):
    min_time = float('inf')  # 고슴도치의 최소 이동 거리
    water_lst = deque()      # 물의 위치를 표시할 q 초기화
    q = deque()              # 고슴도치의 위치를 표시할 q 초기화

    # 비버의 굴과 고슴도치의 위치 찾기
    for r in range(row):
        for l in range(col):
            # S: 고슴도치의 위치, '*': 물의 위치
            if mp[r][l] == 'S':
                q.append((r, l, 0))
            elif mp[r][l] == '*':
                water_lst.append((r, l))

    while q:
        # 물 이동하기
        for _ in range(len(water_lst)):  # 현재 확장할 물의 칸만큼 반복
            i, j = water_lst.popleft()  # 현재 물의 칸
            for k in range(4):  # 사방 탐색
                nx_i, nx_j = i + dx[k], j + dy[k]  # 물이 찰 예정인 칸
                if nx_i < 0 or nx_i >= row or nx_j < 0 or nx_j >= col or mp[nx_i][nx_j] != '.':  # 범위 확인
                    continue
                mp[nx_i][nx_j] = '*'  # 물로 채우기
                water_lst.append((nx_i, nx_j))  # 다음 확장한 물의 칸 표시하기

        for _ in range(len(q)):
            cnt_x, cnt_y, time = q.popleft()
            # 고슴도치 이동하기
            for k in range(4):  # 사방 탐색
                # 고슴도치가 이동할 수 있는 칸인지와 물이 찰 예정인지 확인하기 위한 좌표 이동
                nxt_x, nxt_y = cnt_x + dx[k], cnt_y + dy[k]

                # 이동 가능한 칸인지 확인 + 다음 칸이 이동가능한 칸('.')이거나 두더지의 소굴('D')인지 확인
                if nxt_x < 0 or nxt_x >= row or nxt_y < 0 or nxt_y >= col or mp[nxt_x][nxt_y] in ['X', '0', '*']:
                    continue

                # 기저 조건( 두더지의 소굴('D')이라면 최소값 확인 후 종료 )
                if mp[nxt_x][nxt_y] == 'D':
                    min_time = min(min_time, time + 1)
                    return min_time

                # 물이 찰 예정인지 확인
                tmp_x, tmp_y = nxt_x + dx[k], nxt_y + dy[k]
                if 0 <= tmp_x < row and 0 <= tmp_y < col and mp[tmp_x][tmp_y] == '*':  # 이동 가능한 칸인데 물('*')이라면 패스
                    continue

                mp[nxt_x][nxt_y] = '0'  # 고슴도치의 방문 표시
                q.append((nxt_x, nxt_y, time + 1))
    return 'KAKTUS'


# row: 행의 수, column: 열의 수
row, col = map(int, input().split())
# mp: 고슴도치의 이동 맵
mp = [list(input()) for _ in range(row)]

answer = bfs(mp)
print(answer)  # 답 출력
