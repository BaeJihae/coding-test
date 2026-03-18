import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline())

# 소수인지 아닌지 판별하는 함수
def is_decimal(num):
    for i in range(3, int(num / 2 + 1), 2):
        if num % i == 0:
            return False
    
    return True

# 재귀함수
def dfs(x, d):
    if is_decimal(x):
        if d == n:
            write(str(x) + "\n")
            return
        for i in range(1, 10, 2):
            dfs(x * 10 + i, d + 1)

for k in [2, 3, 5, 7]:
    dfs(k, 1)