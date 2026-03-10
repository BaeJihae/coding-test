import sys
from queue import PriorityQueue

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # n

# 우선순위 큐 선언
myQueue = PriorityQueue()

for _ in range(n):
    x = int(readline())
    if x == 0:
        # 출력
        if myQueue.empty():
            print(0)
        else:
            print(myQueue.get()[1])
    else:
        # 절댓값을 기준으로 정렬하고, 같으면 음수 우선 정렬하도록 조건 설정
        myQueue.put((abs(x), x))