# 계수 정렬

import sys

input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
count = [0] * (N+1)
numbers = list(map(int, input().split()))

for number in numbers:
    count[number] += 1

for i in range(1, N + 1):
    if count[i] != 0:
        for c in range(0, count[i]):
            print(str(i) + ' ')