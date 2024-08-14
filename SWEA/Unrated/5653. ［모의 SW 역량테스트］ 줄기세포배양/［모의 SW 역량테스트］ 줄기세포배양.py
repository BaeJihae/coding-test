# 줄기세포배양

# 세포의 상태를 저장하는 클래스
class Cell:
    def __init__(self, life_cycle):
        self.life_cycle = life_cycle
        self.active = life_cycle
        # 활성 : 1, 비활성 : 0, 죽음 : -1
        self.status = 0

    def reduce_active(self):
        self.active -= 1

    def update_life_cycle(self):
        if self.status != -1:
            self.reduce_active()

    def update_status(self):
        if self.active == 0:
            if self.status == 1:
                self.status = -1
            elif self.status == 0:
                self.status = 1
                self.active = self.life_cycle

    def can_breed(self):
        return self.status == 1 and self.active == self.life_cycle

    def is_count(self):
        return self.status == 1 or self.status == 0


def stem_cell_culture():
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]

    # 배양 용기 크기 설정
    culture_grid = [[None] * (M + 2 * K) for _ in range(N + 2 * K)]

    # 초기 상태 설정
    for i in range(N):
        for j in range(M):
            life_cycle = lst[i][j]
            if life_cycle != 0:
                culture_grid[i + K][j + K] = Cell(lst[i][j])

    # 번식 함수
    def breed_cell(x, y, life_cycle):
        dx = [0, 1, -1, 0]
        dy = [1, 0, 0, -1]

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N + 2 * K and 0 <= ny < M + 2 * K:
                if culture_grid[nx][ny] is None:
                    culture_grid[nx][ny] = Cell(life_cycle)
                    current_breed_xy.append((nx, ny))
                elif (nx, ny) in current_breed_xy:
                    if culture_grid[nx][ny].life_cycle < life_cycle:
                        culture_grid[nx][ny] = Cell(life_cycle)

    # 시뮬레이션
    for k in range(K):
        to_breed = []
        current_breed_xy = []
        for x in range(N + 2 * K):
            for y in range(M + 2 * K):
                if culture_grid[x][y] is not None:
                    if culture_grid[x][y].can_breed():
                        to_breed.append((x, y, culture_grid[x][y].life_cycle))
                    culture_grid[x][y].update_life_cycle()
                    culture_grid[x][y].update_status()

        for x, y, life_cycle in to_breed:
            breed_cell(x, y, life_cycle)

    # 살아있는 줄기 세포 계산
    answer = 0
    for x in range(N + 2 * K):
        for y in range(M + 2 * K):
            if culture_grid[x][y] is not None and culture_grid[x][y].is_count():
                answer += 1

    return answer

# 실행
for tc in range(1, int(input()) + 1):
    count = stem_cell_culture()
    print(f'#{tc} {count}')
