import sys
sys.setrecursionlimit(100000)
MOD = 1000000007

def factorial(s, e):
    result = 1

    for i in range(s, e + 1):
        result *= i
        result %= MOD

    return result

def split_up(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a % MOD

    x = split_up(a, n // 2)
    x = x * x % MOD
    if n % 2 != 0:
        x = x * a % MOD
    return x

N, K = map(int, input().split())
A = factorial(N - K + 1, N)
B = factorial(1, K)
print(A * split_up(B, MOD - 2) % MOD)