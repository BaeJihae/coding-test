# a = str(input())

# col = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# # 위치에 따른 이동 경우의 수
# case = [[2, 3, 4, 4, 4, 4, 3, 2],\
#         [3, 4, 6, 6, 6, 6, 4, 3],\
#         [4, 6, 8, 8, 8, 8, 6, 4],\
#         [4, 6, 8, 8, 8, 8, 6, 4],\
#         [4, 6, 8, 8, 8, 8, 6, 4],\
#         [4, 6, 8, 8, 8, 8, 6, 4],\
#         [3, 4, 6, 6, 6, 6, 4, 3],\
#         [2, 3, 4, 4, 4, 4, 3, 2]]

# for i in range(len(col)):
#     if col[i] in a:
#         a_col = i

# for j in range(8):
#     if str(j) in a:
#         a_row = j-1

# print(case[a_row][a_col])

a = str(input())
a_row = int(a[1])-1
a_col = int(ord(a[0])) - int(ord('a'))

cases = [(-2, -1), (-2, 1), (2, 1), (2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]

count = 0
for case in cases:
    b_row = a_row + case[0]
    b_col = a_col + case[1]
    if -1 < b_row < 8 and -1 < b_col < 8:
        count += 1

print(count)
