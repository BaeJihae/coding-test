n, k = map(int, input().split())

x = 1
y = 1
if k == 0 or n == k:
    print(1)
else:
    if k > n // 2:
        k = n - k

    for _ in range(k):
        x *= n
        n -= 1

    for b in range(1, k + 1):
        y *= b

    print(x // y)
