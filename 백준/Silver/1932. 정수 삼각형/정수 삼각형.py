n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = lst[-1]

for i in range(len(lst) - 2, -1, -1):
    for j in range(len(lst[i])):
        dp[j] = lst[i][j] + max(dp[j], dp[j + 1])

print(dp[0])