import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # 시험을 본 과목의 개수
results = list(map(int, readline().split())) # 각 과목의 시험 성적
maxResults = max(results) # 과목의 최댓값

write(str(sum(results) / maxResults * 100 / n))