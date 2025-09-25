import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coin_costs = list(map(int, input().split()))
    M = int(input())
    
    dp = [0] * (M + 1)
    dp[0] = 1
    
    for c in coin_costs:
        for k in range(c, M + 1):
            dp[k] += dp[k - c]
    print(dp[M])