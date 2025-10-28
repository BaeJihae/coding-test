N, M = map(int, input().split())
p_lst = list(map(int, input().split()))

answer = 0

arr = [0] * (N+1)
for i in range(M-1):
    arr[min(p_lst[i], p_lst[i + 1]) - 1] += 1
    arr[max(p_lst[i], p_lst[i + 1]) - 1] -= 1

for i in range(N-1):
    arr[i + 1] = arr[i] + arr[i + 1]

arr = arr[:-2]

for n in arr:
    if n == 0:
        input()
        continue
    else:
        A, B, C = map(int, input().split())
        answer += min(n * A, n * B + C)

print(answer)