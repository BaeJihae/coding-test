import sys
from heapq import heappush, heappop

input = lambda: sys.stdin.readline().rstrip()

minq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x:
        heappush(minq, x)
    else:
        if minq:
            print(heappop(minq))
        else:
            print(0)