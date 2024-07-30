mtrx_mx = 0
max_i, max_j = 0, 0
for i in range(9):
    lst = list(map(int, input().split()))
    for j in range(9):
        if mtrx_mx < lst[j]:
            max_i, max_j = i, j
            mtrx_mx = lst[j]

print(mtrx_mx)
print(max_i+1, max_j+1)