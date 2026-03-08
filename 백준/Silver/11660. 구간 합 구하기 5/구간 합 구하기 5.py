# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.
# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.
# 1	2 3 4
# 2	3 4 5
# 3	4 5 6
# 4	5 6 7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.
# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

import sys

readline = sys.stdin.readline
write = sys.stdout.write

n, quizNum = map(int, readline().split())   # 2차원의 배열의 크기, 구간 합 질의의 개수

# NxN 개의 수
mapList = [list(map(int, readline().split())) for _ in range(n)]

# 이차원 구간 합 구하기
sum2ndList = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i > 0 and j > 0:
            sum2ndList[i][j] = sum2ndList[i-1][j] + sum2ndList[i][j-1] - sum2ndList[i-1][j-1] + mapList[i][j]
        elif i > 0:
            sum2ndList[i][j] = sum2ndList[i-1][j] + mapList[i][j]
        elif j > 0:
            sum2ndList[i][j] = sum2ndList[i][j-1] + mapList[i][j]
        else:
            sum2ndList[i][j] = mapList[i][j]

# 구간 합 구하기
for _ in range(quizNum):
    x1, y1, x2, y2 = map(int, readline().split())
    if x1 == 1 and y1 == 1:
        write(str(sum2ndList[x2 - 1][y2 - 1]) + '\n')
    elif x1 == 1:
        write(str(sum2ndList[x2 - 1][y2 - 1] - sum2ndList[x2 - 1][y1 - 2]) + '\n')
    elif y1 == 1:
        write(str(sum2ndList[x2 - 1][y2 - 1] - sum2ndList[x1 - 2][y2 - 1]) + '\n')
    else:
        write(str(sum2ndList[x2 - 1][y2 - 1] - sum2ndList[x1 - 2][y2 - 1] - sum2ndList[x2 - 1][y1 - 2] + sum2ndList[x1 - 2][y1 - 2]) + '\n')