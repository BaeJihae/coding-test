# 주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 “좋다(GOOD)”고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # 수의 개수 N
A = list(map(int, readline().split())) # n개의 수의 값
A.sort()
answer = 0

# 주몽의 명령 투포인트 정렬 알고리즘 * n
# 정렬 알고리즘을 사용할 때 자기 자신의 좌표는 건너띄어야 한다.
for i in range(n):
    start_Index, end_Index = 0, n - 1
    
    if i == 0:
        start_Index = 1
    elif i == n - 1:
        end_Index = n - 2
    
    while start_Index < end_Index:
        currentSum = A[start_Index] + A[end_Index]
        if currentSum == A[i]:
            answer += 1
            break
        elif currentSum < A[i]:
            start_Index += 1
        else:
            end_Index -= 1
        
        if start_Index == i:
            start_Index += 1
        if end_Index == i:
            end_Index -= 1

write(str(answer))