# 수 N개가 주어졌을 때, i번째 수부터 j번째 수까지 합을 구하는 프로그램을 작성하시오.
import sys

readline = sys.stdin.readline
write = sys.stdout.write

n, q = map(int, readline().split()) # 데이터의 개수, 질의 개수
numbers = list(map(int, readline().split()))    # 구간 합을 구할 대상 배열

# i 배열까지의 합 구하기
sumList = [0, numbers[0]]

for i in range(1, n):
    sumList.append(sumList[i] + numbers[i])

# 구간 합 구하기
for _ in range(q):
    n1, n2 = map(int, readline().split())
    write(str(sumList[n2]-sumList[n1-1]) + '\n')