# 크기가 N인 수열 A = A1, A2, ..., AN이 있다. 수열의 각 원소 Ai에 대해서 오큰수 NGE(i)를 구하려고 한다.
# Ai의 오큰수는 오른쪽에 있으면서 Ai보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다. 그러한 수가 없는 경우에 오큰수는 -1이다.

# 예를 들어, A = [3, 5, 2, 7]인 경우 NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1이다.
# A = [9, 5, 4, 8]인 경우에는 NGE(1) = -1, NGE(2) = 8, NGE(3) = 8, NGE(4) = -1이다.

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