import sys

input = sys.stdin.readline

m = int(input())
bits = 0

for _ in range(m):
    cmd, *num = input().split()
    if num:
        num = int(num[0]) - 1
        if cmd == 'check':
            print(1 if 1 << num & bits else 0)
            pass
        elif cmd == 'add':
            bits = bits | 1 << num
        elif cmd == 'remove':
            bits = bits & ~(1 << num)
        elif cmd == 'toggle':
            bits = bits & ~(1 << num) if 1 << num & bits else bits | 1 << num
    else:
        if cmd == 'all':
            bits = (1 << 21) - 1
        elif cmd == 'empty':
            bits = 0
