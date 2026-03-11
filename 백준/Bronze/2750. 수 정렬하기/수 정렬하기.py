import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # n

L = list()
for _ in range(N):
    L.append(int(readline()))

L.sort()

for l in L:
    write(str(l) + '\n')    