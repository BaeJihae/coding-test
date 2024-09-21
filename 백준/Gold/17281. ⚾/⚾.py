import sys
from itertools import permutations
input = lambda: sys.stdin.readline().rstrip()

# 입력
n = int(input())  # 이닝 개수
# 각 이닝별 선수들의 결과
result_by_inning = [list(map(int, input().split())) for _ in range(n)]


def game_start(player_order):
    score = 0  # 점수
    order = 0  # 현재 타순의 인덱스 값

    for inning in result_by_inning:
        p1 = p2 = p3 = 0  # 1루, 2루, 3루의 상태 ( 0: 없음, 1: 있음 )
        out_cnt = 0  # 아웃된 횟수

        # 이닝 별 게임
        while out_cnt < 3:  # 3진 아웃 -> 이닝 종료
            current_player = player_order[order % 9]  # 현재 선수 번호
            player_result = inning[current_player]  # 현재 선수의 결과

            if player_result == 0:  # 아웃일 때,
                out_cnt += 1  # 아웃 + 1
            elif player_result == 1:  # 안타일 때,
                score += p3
                p1, p2, p3 = 1, p1, p2
            elif player_result == 2:  # 2루타일 때,
                score += p3 + p2
                p1, p2, p3 = 0, 1, p1
            elif player_result == 3:  # 3루타일 때,
                score += p3 + p2 + p1
                p1, p2, p3 = 0, 0, 1
            else:  # 홈런일 때,
                score += p3 + p2 + p1 + 1
                p1, p2, p3 = 0, 0, 0
            order += 1  # 선수 교체

    return score


def solution():
    max_score = 0
    for player_order in permutations(range(1, 9), 8):
        player_order = list(player_order)
        player_order.insert(3, 0)
        max_score = max(max_score, game_start(player_order))

    return max_score


print(solution())
