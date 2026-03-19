import sys
readline = sys.stdin.readline

N = int(readline())     # 데이터의 개수
A = list(map(int, readline().split())) # 데이터 리스트

M = int(readline())     # 찾아야 할 숫자의 개수
S = list(map(int, readline().split())) # 찾아야 할 숫자 리스트

# 리스트 A 정렬
A.sort()

def binary_search(x, i, j):
    global result
    
    if i > j:
        return

    m = A[(i + j) // 2]
    if x == m:
        result = True
        return
    elif x < m:
        binary_search(x, i, (i + j) // 2 - 1)
    else:
        binary_search(x, (i + j) // 2 + 1, j)

for x in S:
    result = False
    
    binary_search(x, 0, N - 1)
    
    if result:
        print(1)
    else:
        print(0)