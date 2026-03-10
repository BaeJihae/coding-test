import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # n
A = list(map(int, readline().split()))  # 수열 A

answer = [-1] * n # 정답을 저장할 리스트
stack = []  # (값, 위치)가 들어갈 stack

# 0 ~ n-1 까지 탐색
for i in range(0, n):
    while(True):
        # 만약, 스택에 아무것도 안들어가 있거나 스택의 마지막 값이 들어갈 값보다 클면 추가
        if stack == [] or stack[-1][0] >= A[i]:
            stack.append((A[i], i))
            break
        # 만약, 스택의 마지막 값이 들어갈 값보다 작으면 그 값은 빠지면서 해당 위치에 들어갈 값이 저장
        _, j = stack.pop()
        answer[j] = A[i]

for ans in answer:
    write(str(ans) + ' ')