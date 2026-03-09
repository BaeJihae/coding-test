# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

# M으로 나누어 떨어짐.
# 나머지 연산자는 분배법칙이 가능함. +, -, * 까지
# (A1 + A2) % M = A1 % M + A2 % M // (A1 - A2) % M = A1 % M - A2 % M
# 누적합 => 나머지 연산자 

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n, m = map(int, readline().split())
lst = list(map(int, readline().split()))

tempList = [0] * m  # 나머지 값의 개수를 저장할 리스트

# 1. 누적합 구하기
sumList = [lst[0]]
for i in range(1, n):
    sumList.append(sumList[i - 1] + lst[i])

# 2. 누적합 리스트의 m으로 나눈 나머지 구하기
for i in range(0, n):
    # 3. 나머지 값 개수 저장하기6
    temp = sumList[i] % m
    tempList[temp] += 1
    sumList[i] = temp

# 4. 구간 합의 나머지 갯수 구하기
answer = tempList[0] 
for num in tempList:
    if num:
        answer += num * (num - 1) // 2

write(str(answer))