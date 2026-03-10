import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # n
queue = deque()

for i in range(1, n+1):
    queue.append(i)

while(len(queue) != 1):
    queue.popleft()
    queue.append(queue.popleft())

write(str(queue.pop()))