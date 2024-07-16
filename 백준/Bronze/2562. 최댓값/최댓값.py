list = []
for _ in range(9):
    list.append(int(input()))

max_num = max(list)
print(max_num)
print(list.index(max_num)+1)