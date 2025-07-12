import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N = int(input())

# 모든 강의실 리스트
class_lst = []

for _ in range(N):
    S, T = map(int, input().split())
    class_lst.append((S, T))

# class_lst 정렬
class_lst.sort()

# 강의실의 끝나는 값을 저장할 우선순위 큐
q = []

# 필요한 강의실 개수
answer = 0

for S, T in class_lst:
    if q and S >= q[0]:
        heappop(q)
    else:
        answer += 1
    heappush(q, T)

print(answer)