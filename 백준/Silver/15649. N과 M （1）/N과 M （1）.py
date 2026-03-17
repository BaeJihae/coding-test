import sys

readline = sys.stdin.readline
write = sys.stdout.write

N, M = map(int, readline().split())

visited = [0] * (N + 1)

def back(n, depth):
    if depth == M:
        for i in str(n):
            write(i + " ")
        write("\n")
    
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = 1
            back(n*10 + i, depth + 1)
            visited[i] = 0

for i in range(1, N + 1):
    visited[i] = 1
    back(i, 1)
    visited[i] = 0