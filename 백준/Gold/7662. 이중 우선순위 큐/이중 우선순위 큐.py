import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

for tc in range(int(input())):
    k = int(input())  # 연산 개수
    minQ, maxQ = [], []
    deleted = [True] * k
    for i in range(k):
        cmd, num = input().split()
        num = int(num)
        if cmd == 'I':
            heappush(minQ, (num, i))
            heappush(maxQ, (-num, i))
            deleted[i] = False
        else:
            if num == 1:
                while maxQ and deleted[maxQ[0][1]]:
                    heappop(maxQ)
                if maxQ:
                    deleted[maxQ[0][1]] = True
                    heappop(maxQ)
            else:
                while minQ and deleted[minQ[0][1]]:
                    heappop(minQ)
                if minQ:
                    deleted[minQ[0][1]] = True
                    heappop(minQ)

    while minQ and deleted[minQ[0][1]]:
        heappop(minQ)
    while maxQ and deleted[maxQ[0][1]]:
        heappop(maxQ)

    if maxQ and minQ:
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')