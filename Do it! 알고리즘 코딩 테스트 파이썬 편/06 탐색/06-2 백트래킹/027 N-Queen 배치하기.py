N = int(input())

answer = 0

# 대각선 검사를 위한 배열 2가지
right_up_checking = [0] * (N * 2 - 1)
right_down_checking = [0] * (N * 2 - 1)

# 세로 검사를 위한 배열
down_checking = [0] * N

def backtracking(i):
    global answer
    
    if i == N:
        answer += 1
        return
    
    for j in range(N):
        # 유효성 검사 및 가지치기
        if not down_checking[j] and not right_up_checking[i + j] and not right_down_checking[i - j + N - 1]:
            down_checking[j] = 1
            right_up_checking[i + j] = 1
            right_down_checking[i - j + N - 1] = 1
            
            backtracking(i + 1)
            
            down_checking[j] = 0
            right_up_checking[i + j] = 0
            right_down_checking[i - j + N - 1] = 0
    return

backtracking(0)
print(answer)