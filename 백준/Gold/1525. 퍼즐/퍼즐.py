import sys
from collections import deque

input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution():
    # 문자열로 입력 받기
    str_3x3 = ''
    for _ in range(3):
        str_3x3 += ''.join(list(input().split()))

    search_0 = str_3x3.index('0')  # 0 위치 찾기
    q = deque([(search_0 // 3, search_0 % 3, 0, str_3x3)])  # bfs 진행할 큐 초기화
    visited = {str_3x3: 0}  # 방문 체크

    while q:
        i, j, k, cnt_str = q.popleft()  # i: 행번호, j: 열번호, k: 이동 횟수, cnt_lst: 현재 리스트

        # 기저 조건
        if cnt_str == '123456780':
            return k

        # 사방 탐색
        for d in range(4):
            nxt_i, nxt_j = i + dx[d], j + dy[d]  # 이동할 위치
            if 0 <= nxt_i < 3 and 0 <= nxt_j < 3:  # 이동 가능 여부 확인
                cnt_lst = list(cnt_str)
                cnt_lst[i * 3 + j], cnt_lst[nxt_i * 3 + nxt_j] = cnt_lst[nxt_i * 3 + nxt_j], cnt_lst[i * 3 + j]
                nxt_str = ''.join(cnt_lst)

                if visited.get(nxt_str, 0) == 0:
                    visited[nxt_str] = k + 1
                    q.append((nxt_i, nxt_j, k + 1, nxt_str))

    return -1


print(solution())
