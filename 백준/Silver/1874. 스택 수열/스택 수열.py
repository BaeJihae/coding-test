import sys
from collections import deque

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # n
stack = []  # 수열을 만들기 위한 stack
answer = [] # +, -를 저장하기 위한 리스트

i = 1 # 증가할 수
for _ in range(n):
    a = int(readline()) # 비교할 대상
    
    while(i <= n + 1):
        if stack and stack[-1] == a:
            stack.pop()
            answer.append('-')
            break
    
        stack.append(i)
        answer.append('+')
        i += 1

if stack:
    write("NO")
else:
    for ans in answer:
        write(ans + '\n')