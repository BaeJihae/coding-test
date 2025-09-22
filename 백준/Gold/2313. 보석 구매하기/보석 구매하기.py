import math

n = int(input())
answer = 0
answer_lst = [(0, 0, 0)]*n

for x in range(n):
    L = int(input())
    jewel_lst = list(map(int, input().split()))

    sum_lst = [0] * L
    mx = -math.inf

    for i in range(L):
        sum_i = sum(jewel_lst[:i+1])
        if sum_i > mx:
            mx = sum_i
            answer_lst[x] = (1, i + 1, i + 1)
        sum_lst[i] = sum_i

    for k in range(L-1):
        for l in range(k+1, L):
            sum_lst[l] -= jewel_lst[k]
            if sum_lst[l] > mx:
                mx = sum_lst[l]
                answer_lst[x] = (k + 2, l + 1, l - k)
            elif sum_lst[l] == mx and answer_lst[x][2] > (l-k):
                answer_lst[x] = (k + 2, l + 1, l - k)

    answer += mx

print(answer)
for a, b, _ in answer_lst:
    print(a, b)