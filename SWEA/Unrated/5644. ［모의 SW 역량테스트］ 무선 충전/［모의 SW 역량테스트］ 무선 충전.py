# 무선 충전
for tc in range(1, int(input()) + 1):
    M, N = map(int, input().split())

    # 안함0, 상1, 우2, 하3, 좌4
    D = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

    # A, B의 이동루트
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # A개의 AP 정보
    AP = []
    for _ in range(N):
        AP.append(tuple(map(int, input().split())))

    # 전체 에너지
    answer = 0


    # 두 좌표 사이의 거리 구하기
    def distance(ax, ay, bx, by):
        return abs(ax - bx) + abs(ay - by)


    # 동일한 지점이 있을 때의 최댓값 비교
    def compare_max(arr1, arr2):
        mx = 0

        for i in arr1:
            for j in arr2:
                if i == j:
                    sm = AP[i][3]
                else:
                    sm = (AP[i][3] + AP[j][3])

                mx = max(mx, sm)

        return mx


    ai, aj, bi, bj = 1, 1, 10, 10

    for k in range(M + 1):

        # 현재 위치에서의 값 비교를 통한 충전 양 도출
        BC_a, BC_b = [], []
        for num in range(N):
            if distance(AP[num][0], AP[num][1], ai, aj) <= AP[num][2]:
                BC_a.append(num)

            if distance(AP[num][0], AP[num][1], bi, bj) <= AP[num][2]:
                BC_b.append(num)

        if BC_a and BC_b:
            answer += compare_max(BC_a, BC_b)
        elif BC_a:
            answer += max([AP[i][3] for i in BC_a])
        elif BC_b:
            answer += max([AP[i][3] for i in BC_b])

        if k == M:
            break

        # 이동
        ai += D[A[k]][0]
        aj += D[A[k]][1]

        bi += D[B[k]][0]
        bj += D[B[k]][1]

    print(f'#{tc} {answer}')
