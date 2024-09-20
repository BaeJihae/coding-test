# 성곽
import sys
from collections import deque
input = lambda: sys.stdin.readline().strip()

# 서 : 1, 북 : 2, 동 : 4, 남 : 8
directions = ((0, -1), (-1, 0), (0, 1), (1, 0))

# 입력
n, m = map(int, input().split())
castle_board = [list(map(int, input().split())) for _ in range(m)]


# 방 크기 사이즈를 구하는 함수
# num: 임시 방 번호, visited: 방문체크할 2차원 배열, new_castle_board : 방 번호를 적어줄 2차원 배열
def count_room_size(x, y, num, visited, new_castle_board):
    cnt = 1  # 방 크기
    queue = deque([(x, y)])  # 현재 좌표로 큐 초기화
    visited[x][y] = True  # 현재 위치 방문 체크
    while queue:
        cx, cy = queue.popleft()
        new_castle_board[cx][cy] = num  # 방 번호 매기기
        for d in range(4):  # 사방 탐색 ( 0: 서, 1: 북, 2: 동, 3: 남 )
            if not castle_board[cx][cy] & 1 << d:  # 비트연산자를 통한 뚫려있는 길인지 확인
                nx, ny = cx + directions[d][0], cy + directions[d][1]  # 뚫려있다면 다음 좌표로 이동
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:  # 범위에 맞고, 방문하지 않았다면
                    visited[nx][ny] = True  # 방문 체크
                    queue.append((nx, ny))  # 다음에 다시 방문하기 위해 큐에 추가
                    cnt += 1  # 방 크기 + 1
    # 방 크기 출력
    return cnt


# 두 개의 방의 합을 출력하기 위한 함수
def expant_room(x, y):
    sum_two_room = 0  # 두 개의 방의 합
    for dx, dy in ((0, 1), (1, 0)):  # 좌, 하만 탐색
        nx, ny = x + dx, y + dy  # 좌표 이동
        if 0 <= nx < m and 0 <= ny < n and new_castle_board[x][y] != new_castle_board[nx][ny]:  # 범위에 맞고, 방 번호가 다르다면
            sum_two_room = max(sum_two_room, room_dict[new_castle_board[x][y]] + room_dict[
                new_castle_board[nx][ny]])  # 두 방의 크기를 합하여 최댓값 비교
    return sum_two_room


visited = [[False] * n for _ in range(m)]  # 방문 체크할 배열
room_cnt, max_room_size = 0, 0  # 방의 개수, 최대 방의 크기
room_dict = {}  # 방의 번호에 따른 방의 크기를 정의하는 딕셔너리
new_castle_board = [[-1] * n for _ in range(m)]  # 방 번호를 적어줄 2차원 배열

# 방 탐색
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            x = count_room_size(i, j, room_cnt, visited, new_castle_board)
            room_dict[room_cnt] = x
            max_room_size = max(max_room_size, x)  # 최대 방의 크기 구하기
            room_cnt += 1  # 방의 개수 + 1

max_sum_two_room_size = 0  # 두 개의 방의 합의 최댓값
for x in range(m):
    for y in range(n):
        max_sum_two_room_size = max(max_sum_two_room_size, expant_room(x, y))

print(room_cnt)  # 방의 개수 출력
print(max_room_size)  # 최대 방의 크기 출력
print(max_sum_two_room_size)  # 두 개의 방을 합친 최댓값 출력
