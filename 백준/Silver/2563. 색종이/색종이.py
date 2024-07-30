painted_lst = [ [0 for _ in range(100)] for _ in range(100)]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())

    for i in range(a, a+10):
        for j in range(b, b+10):
            if 0 < i <= 100 and 0 < j <= 100:
                painted_lst[i-1][j-1] = 1

count = 0

for i in range(100):
    for j in range(100):
        if painted_lst[i][j] == 1:
            count += 1

print(count)