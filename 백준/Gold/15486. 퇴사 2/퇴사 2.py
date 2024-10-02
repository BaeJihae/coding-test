n = int(input())
dp = [0] * (n + 1)
for i in range(1, n+1):
    t, p = map(int, input().split())
    if i + t - 1 <= n and dp[i + t - 1] < dp[i - 1] + p:
        dp[i + t - 1] = dp[i - 1] + p

    dp[i] = max(dp[i-1], dp[i])

print(dp[n])