import sys

from collections import deque

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())  # N : 행의 개수, M : 열의 개수
map_data = [list(map(int, input())) for _ in range(N)]  # 주어진 숫자 맵 ( 0: 갈 수 있는 길, 1: 벽 )


# map_data : 주어진 숫자 맵, start_x: 시작 x좌표, start_y: 시작 y좌표, end_x: 종료 x좌표, end_y: 종료 y좌표
def bfs(map_data, start_x, start_y, end_x, end_y):
    queue = deque([(0, start_x, start_y)])  # 큐 초기화 (벽 통과 유무, x좌표, y좌표)
    visited = [[[0] * M for _ in range(N)] for _ in range(2)]  # 방문 유무와 함께 경로의 길이를 저장할 배열
    visited[0][start_x][start_y] = 1  # 첫 방문 표시

    while queue:
        k, cx, cy = queue.popleft()  # k: 벽 통과 유무 ( 0: 벽 통과X, 1: 벽 통과O )
        if cx == end_x and cy == end_y:  # 기저 조건 ( 현재 좌표가 종료 좌표와 같다면 종료 )
            # 벽 통과를 했다면 벽 통과한 배열을 출력하지만 벽 통과를 하지 않았다면 벽 통과를 하지 않은 배열 출력 
            return visited[1][cx][cy] if visited[1][cx][cy] else visited[0][cx][cy]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # 사방 탐색
            nx, ny = cx + dx, cy + dy  # 다음 좌표
            if 0 <= nx < N and 0 <= ny < M:  # 방문 가능 확인
                if map_data[nx][ny] == 0 and not visited[k][nx][ny]:  # 0이고, 방문하지 않은 곳이라면
                    visited[k][nx][ny] = visited[k][cx][cy] + 1  # 이전 경로 + 1
                    queue.append((k, nx, ny))  # 큐에 저장
                elif map_data[nx][ny] == 1 and k == 0 and not visited[1][nx][ny]:  # 현재 벽 통과를 하지 않았다면,
                    visited[1][nx][ny] = visited[0][cx][cy] + 1  # 이전 경로 + 1
                    queue.append((1, nx, ny))  # 큐에 저장
    return -1  # 최단 경로가 출력되지 않을 경우


# 정답 출력
print(bfs(map_data, 0, 0, N - 1, M - 1))
