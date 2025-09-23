import sys
input = sys.stdin.readline

N, T = map(int, input().split())
problems = [tuple(map(int, input().split())) for _ in range(N)]
problems.sort()

dp = [0] * (T + 1)

# k: 공부 시간, 단원 문제의 배점
for k, s in problems:
    for current_time in range(T, k - 1, -1):
        dp[current_time] = max(dp[current_time], dp[current_time - k] + s)

print(dp[T])
