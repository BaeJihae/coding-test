import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline())
lst = [ int(readline()) for _ in range(N) ]

lst.sort(reverse=True)

for x in lst:
    write(str(x) + "\n")