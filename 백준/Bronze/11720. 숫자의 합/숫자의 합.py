import sys

input = sys.stdin.readline
write = sys.stdout.write

n = int(input()) # 숫자의 개수
numbers = list(input()) # 공백 없이 주어진 N개의 숫자

answer = 0 # 숫자의 합
for i in range(0, n):
    answer += int(numbers[i])

write(str(answer))