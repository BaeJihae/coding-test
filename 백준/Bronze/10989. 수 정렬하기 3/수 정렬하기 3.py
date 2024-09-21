import sys
input = sys.stdin.readline

n = int(input())
answer = [0] * 10_001

for _ in range(n):
    x = int(input())
    answer[x] += 1

for i in range(10001):
    k = answer[i]
    if k:
        for _ in range(k):
            print(i)