n, m = map(int, input().split())

list = [0] * n

for _ in range(m):
    i, j, k = map(int, input().split())
    for x in range(i, j+1):
        list[x-1] = k

for a in list:
    print(a, end=" ")