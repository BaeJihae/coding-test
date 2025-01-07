'''
점화식
N = [N][3] + [N][2] + [N][1]
[N][3] = [N-3][1] + [N-3][2] + [N-3][3]
[N][2] = [N-2][1] + [N-2][2]
[N][1] = [N-1][1] 
'''

tc = int(input())
arr = list()
for _ in range(tc):
    arr.append(int(input()))

mx = max(arr)

# DP 만들기
dp = list()
for _ in range(mx):
    dp.append([0] * 3)

dp[0][0] = 1
dp[1][0] = 1
dp[1][1] = 1
dp[2][0] = 1
dp[2][1] = 1
dp[2][2] = 1

# 점화식에 의한 계산
if mx > 2:
    for i in range(3, mx):
        dp[i][2] = dp[i-3][2] + dp[i-3][1] + dp[i-3][0]
        dp[i][1] = dp[i-2][1] + dp[i-2][0]
        dp[i][0] = dp[i-1][0]

# 정답
for i in arr:
    print(dp[i-1][0] + dp[i-1][1] + dp[i-1][2])
