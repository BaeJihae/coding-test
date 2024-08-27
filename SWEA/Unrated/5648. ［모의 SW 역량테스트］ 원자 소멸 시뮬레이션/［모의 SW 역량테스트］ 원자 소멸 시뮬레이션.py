# 원자 소멸 시뮬레이션


# 방향에 따른 이동 ( 상, 하, 좌, 우 )
dx = [0.0, 0.0, -0.5, 0.5]
dy = [0.5, -0.5, 0.0, 0.0]


# 원자 클래스
class Atom:
    collition = False

    def __init__(self, lst):
        self.x = lst[0]
        self.y = lst[1]
        self.d = lst[2]
        self.e = lst[3]

    def move(self):
        self.x += dx[self.d]
        self.y += dy[self.d]

        if self.x < -1000 or self.x > 1000 or self.y < -1000 or self.y > 1000:
            self.collition = True
            return None

        return (self.x, self.y)

    def isCollision(self):
        self.collition = True


for tc in range(1, int(input()) + 1):
    # 입력
    N = int(input())

    atom_arr = []
    for _ in range(N):
        atom_arr.append(Atom(list(map(int, input().split()))))

    # 에너지의 합
    energy_sum = 0

    for _ in range(4002):
        cnt = 0
        move_xy = {}
        for at in atom_arr:
            if not at.collition:
                xy = at.move()
                if xy is not None:
                    if xy not in move_xy:
                        move_xy[xy] = [at]
                    else:
                        move_xy[xy].append(at)
            else:
                cnt += 1

        if cnt == N:
            break

        for k, v in move_xy.items():
            if len(v) > 1:
                for a in v:
                    energy_sum += a.e
                    a.isCollision()

    # 출력
    print(f'#{tc}', energy_sum)
