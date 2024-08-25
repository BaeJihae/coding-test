N = int(input())

# queen의 N개를 놓을 수 있는 경우의 수
answer = 0

# 열의 조회를 체크할 배열
col_check = [0] * N
# 대각선을 체크할 배열
cross_right_down = [0] * (2 * N - 1)
cross_right_up = [0] * (2 * N - 1)

def dfs(idx):
    global answer

    if idx == N:
        answer += 1
        return

    for i in range(N):
        if not col_check[i] and not cross_right_down[idx - i + (N - 1)] and not cross_right_up[idx + i]:
            col_check[i] = cross_right_down[idx - i + (N - 1)] = cross_right_up[idx + i] = True
            dfs(idx + 1)
            col_check[i] = cross_right_down[idx - i + (N - 1)] = cross_right_up[idx + i] = False

dfs(0)
print(answer)
