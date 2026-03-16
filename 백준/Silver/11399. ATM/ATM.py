import sys

readline = sys.stdin.readline
write = sys.stdout.write

N = int(readline()) # 데이터 개수
P = list(map(int, readline().split())) # 인출하는 데 걸리는 시간


for i in range(1, N):
    for j in range(0, i):
        if P[j] > P[i]:
            # j번째 자리에 i값 넣기
            P = P[:j] + [P[i]] + P[j:i] + P[i+1:]
            break

# 오름차순으로 정렬한 P의 누적합 구하기
answer = 0
sum = 0
for p in P:
    sum += p
    answer += sum 

write(str(answer))