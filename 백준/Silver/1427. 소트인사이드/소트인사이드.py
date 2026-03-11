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