# 세준이는 기말고사를 망쳤다. 세준이는 점수를 조작해서 집에 가져가기로 했다. 
# 일단 세준이는 자기 점수 중에 최댓값을 골랐다. 이 값을 M이라고 한다. 
# 그리고 나서 모든 점수를 점수/M*100으로 고쳤다.
# 예를 들어, 세준이의 최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점이 된다.
# 세준이의 성적을 위의 방법대로 새로 계산했을 때, 새로운 평균을 구하는 프로그램을 작성하시오.

# 1. 최댓값 구하기
# 2. {(x1/M*100)+(x2/M*100)+(x3/M*100)}/3 = (x1+x2+x3)/Max*100/3 이용하기

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n = int(readline()) # 시험을 본 과목의 개수
results = list(map(int, readline().split())) # 각 과목의 시험 성적
maxResults = max(results) # 과목의 최댓값

write(str(sum(results) / maxResults * 100 / n))