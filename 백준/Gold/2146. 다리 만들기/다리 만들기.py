from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip()

# 입력 예시
n = int(input())  # 지도의 크기
map_data = [list(map(int, input().split())) for _ in range(n)]

# 방향 벡터 (하, 우, 상, 좌)
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def blood_fill(x, y, island_id):
    queue = deque([(x, y)])
    map_data[x][y] = island_id  # 현재 위치를 섬 번호로 변경
    bridge_start = set()  # 해안선을 저장할 set 변수

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            # 지도 범위를 벗어나지 않고, 방문하지 않은 섬의 경우
            if 0 <= nx < n and 0 <= ny < n:
                if map_data[nx][ny] == 1:  # 섬 찾기
                    map_data[nx][ny] = island_id  # 섬 번호를 매김
                    queue.append((nx, ny))
                elif map_data[nx][ny] == 0:  # 해안선 찾기
                    bridge_start.add((cx, cy))

    return bridge_start


def bfs(island_id, start_coordinates):
    queue = deque([*start_coordinates])
    distances = [[-1] * n for _ in range(n)]
    for x, y in start_coordinates:
        distances[x][y] = 0

    while queue:
        qx, qy = queue.popleft()
        for dx, dy in directions:
            nx, ny = qx + dx, qy + dy
            if 0 <= nx < n and 0 <= ny < n:
                if map_data[nx][ny] == 0 and distances[nx][ny] == -1:
                    distances[nx][ny] = distances[qx][qy] + 1
                    queue.append((nx, ny))
                elif map_data[nx][ny] != island_id and map_data[nx][ny] > 1:
                    return distances[qx][qy]
    return float('inf')

# 각 섬의 해안선 찾기
island_dict = {}

# 섬 번호 초기화
island_id = 2  # 섬 번호 시작 (1은 지도에서 섬의 초기 값이므로 2부터 시작)

# 모든 지도를 순회하며 섬 찾기
for i in range(n):
    for j in range(n):
        if map_data[i][j] == 1:  # 섬을 찾으면
            bridge_start = blood_fill(i, j, island_id)  # BFS로 섬을 구분하고 번호 매기기
            island_dict[island_id] = bridge_start  # 각 섬에 해안선 추가하기
            island_id += 1  # 다음 섬을 위해 섬 번호 증가

answer = float('inf')

# 각 섬의 해안선으로 시작해 다른 섬을 만날때까지 bfs 탐색을 진행한 후 거리 기록하기
for island_id, start_coordinates in island_dict.items():
    cnt = bfs(island_id, start_coordinates)
    answer = min(cnt, answer)

print(answer)