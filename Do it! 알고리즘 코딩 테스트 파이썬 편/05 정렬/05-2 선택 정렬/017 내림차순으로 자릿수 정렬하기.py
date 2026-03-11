# 배열을 정렬하는 것은 쉽다. 수가 주어지면, 그 수의 각 자리수를 내림차순으로 정렬해보자.

import sys

readline = sys.stdin.readline
write = sys.stdout.write

A = list(map(int, readline()[:-1])) # 정렬할 수

for i, a in enumerate(A):
    A[i] = (a, i)

for i in range(len(A)):
    min_A, j = max(A[i:])
    A[i], A[j] = (min_A, i), (A[i][0], j)

for a in A:
    write(str(a[0]))