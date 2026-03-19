import sys
readline = sys.stdin.readline

N, M = map(int, readline().split())  # 강의 수, 블루레이 최대수
class_list = list(map(int, readline().split()))    # 강의 길이 리스트

# 강의 전체 탐색
max_class = 0
sum_class = 0
for class_time in class_list:
    # 강의 최댓값 구하기
    if class_time > max_class:
        max_class = class_time
    
    # 강의 합 구하기
    sum_class += class_time

# 재귀함수
def recursion(i, j):
    global result
    
    # i 시작 값, j 종료 값, m (시작값 + 종료값) // 2
    m = (i + j) // 2
    
    # if i > j => i 값 출력 후 반복문 종료
    if i > j:
        result = i
        return

    cnt_bluelay = 1 # 블루레이 개수
    sum_bluelay = 0 # 블루레이 저장값
    
    # 반복문 - 강의 탐색
    for class_time in class_list:
        # if 블루레이 개수 > 블루레이 최대수 => 반복문 종료 
        if cnt_bluelay > M:
            break
        
        # if 블루레이 값 + 현재 값 > m 
        if sum_bluelay + class_time > m:
            sum_bluelay = 0     # 블루레이 비우기
            cnt_bluelay += 1    # 블루레이 개수 증가 
        
        # 현재 값 저장
        sum_bluelay += class_time

    # 중간 확인
    # print(f'i = {i}, j = {j}, m = {m}, cnt_bluelay = {cnt_bluelay}')

    if cnt_bluelay <= M:
        recursion(i, m - 1)
    else:
        recursion(m + 1, j)

# 결과값 저장
result = 0
# 재귀함수 실행
recursion(max_class, sum_class)
# 답 도출
print(result)