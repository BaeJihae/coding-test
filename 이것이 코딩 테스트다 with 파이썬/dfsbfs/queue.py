from collections import deque
# deque는 스택과 큐의 장점을 모두 채택한 자료구조

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse()
print(queue) # 나중에 들어온 순서대로 출력

queue = list(queue)
print(queue)