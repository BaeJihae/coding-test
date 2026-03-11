import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # n

L = list()
for i in range(N):
    L.append((int(readline()), i))

sortedL = sorted(L)
answer = 0

for j in range(N):
    if answer < sortedL[j][1] - j:
        answer = sortedL[j][1] - j

print(answer + 1)