# 배열의 주어진 범위의 합을 2로 나눈 몫을 구하세요.

import random
import sys

input = sys.stdin.readline
print = sys.stdout.write

testcase = int(input())
A = [0] * 100001

for i in range(0, 100001):
    A[i] = random.randrange(1, 101)

for t in range(1, testcase + 1):
    answer = 0
    start, end = map(int, input().split())
    
    for x in range(start, end + 1):
        answer = answer + A[x]
        
    print(f'#{t} answer = {str(answer//2)}')

# print(' '.join(map(str, A)))