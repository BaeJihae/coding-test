from collections import defaultdict

N, M = map(int, input().split())
p_lst = list(map(int, input().split()))

dct = defaultdict()
answer = 0

for i in range(M-1):
    if p_lst[i] == p_lst[i+1]:
        continue
    for j in range(min(p_lst[i], p_lst[i + 1]), max(p_lst[i], p_lst[i + 1])):
        dct[j] = dct.get(j, 0) + 1

for n in range(1, N):
    if dct.get(n, 0) != 0:
        A, B, C = map(int, input().split())
        answer += min(dct[n] * A, dct[n] * B + C)
    else:
        input().split()

print(answer)