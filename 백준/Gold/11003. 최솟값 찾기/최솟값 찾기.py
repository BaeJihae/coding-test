import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

N, L = map(int, readline().split()) # 숫자의 개수, 슬라이딩 윈도우의 크기
numbers = [0] + list(map(int, readline().split())) # 숫자 리스트

D = [0] * (N + 1)   # 최솟값 저장
myDeque = deque()   # 최솟값을 관리할 deque

# i = 1 ~ N - 1까지 순환
for i in range(1, N + 1):
    while myDeque and myDeque[-1][1] > numbers[i]:
        myDeque.pop()
    
    myDeque.append((i, numbers[i])) # 3. (i, numbers[i]) 추가
    
    if myDeque[0][0] <= i - L:
        myDeque.popleft()
    
    D[i] = myDeque[0][1]    # 최솟값 증가


for j in range(1, N + 1):
    write(str(D[j]) + " ")