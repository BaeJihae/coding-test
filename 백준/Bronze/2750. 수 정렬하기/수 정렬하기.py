import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # n

L = list()
for _ in range(N):
    L.append(int(readline()))

# 버블 정렬
for i in range(N, 0, -1):
    count = 0
    for j in range(0, i - 1):
        if L[j] > L[j+1]:
            L[j], L[j+1] = L[j+1], L[j]
            count += 1
    if count == 0:
        break

for l in L:
    write(str(l) + '\n')