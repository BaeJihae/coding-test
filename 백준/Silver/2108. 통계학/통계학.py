import sys
from collections import Counter

n = int(sys.stdin.readline())

# n 개의 숫자를 입력받아 리스트에 저장하기

num_list = [int(sys.stdin.readline()) for _ in range(n)]


# 산술 평균 출력

print(int(round(sum(num_list)/n, 0)))


# 중앙값 출력

num_list.sort()
print(num_list[int(n/2)])


# 최빈값 출력

mode = Counter(num_list)
mode_most_list = mode.most_common(2)
if len(mode_most_list) == 1:
    print(mode_most_list[0][0])
else:
    if mode_most_list[0][1] == mode_most_list[1][1]:
        print(mode_most_list[1][0])
    else:
        print(mode_most_list[0][0])


# 최댓값과 최솟값의 차이 출력

print(abs(max(num_list)-min(num_list)))