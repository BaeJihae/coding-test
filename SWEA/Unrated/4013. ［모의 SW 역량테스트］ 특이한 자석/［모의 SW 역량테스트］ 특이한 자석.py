from collections import deque

direc = {-1: 1, 1: -1}


# 자석 점수 계산
def calculate_score(magnet, num):
    if magnet:  # 자석이 S극
        return 2 ** num
    else:  # 자석이 N극
        return 0


# 자석 회전
def magnetic_rotation(change_direction, num, magnet_lst, d, visited):
    visited[num] = True

    if d == 1:  # 시계 방향
        magnet_lst[num].appendleft(magnet_lst[num].pop())
    else:  # 시계 반대 방향
        magnet_lst[num].append(magnet_lst[num].popleft())

    if num - 1 >= 0 and [num - 1, num] in change_direction and not visited[num - 1]:
        magnetic_rotation(change_direction, num - 1, magnet_lst, direc[d], visited)

    if num + 1 < 4 and [num, num + 1] in change_direction and not visited[num + 1]:
        magnetic_rotation(change_direction, num + 1, magnet_lst, direc[d], visited)


# 주어진 회전만큼 자석 회전 후 자석들의 점수 합계를 반환하는 함수
def solution(magnet_lst, lst):
    # K만큼 자석 회전
    for num, direction in lst:
        # 붙어있는 자성이 다른지 확인
        change_direction = []
        for i in range(3):
            if magnet_lst[i][2] != magnet_lst[i + 1][-2]:
                change_direction.append([i, i + 1])
        visited = [False] * 4  # 방문 체크
        magnetic_rotation(change_direction, num - 1, magnet_lst, direction, visited) # 자석 회전

    # 회전이 끝난 후에 점수 구하기
    score_sum = 0
    for i in range(4):
        score_sum += calculate_score(magnet_lst[i][0], i)
    return score_sum


for tc in range(1, int(input()) + 1):
    K = int(input())  # 자석을 회전시키는 횟수

    magnetic_lst = [deque(map(int, input().split())) for _ in range(4)]

    lst = []
    for _ in range(K):
        lst.append(list(map(int, input().split())))

    answer = solution(magnetic_lst, lst)

    print(f'#{tc} {answer}')