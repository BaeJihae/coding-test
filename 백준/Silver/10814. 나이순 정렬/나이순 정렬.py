import sys
input = sys.stdin.readline

n = int(input())
arr = [None] * 201
for _ in range(n):
    age, name = input().split()
    age = int(age)
    if arr[age]:
        arr[age].append(name)
    else:
        arr[age] = [name]

for i in range(201):
    if arr[i]:
        name_arr = arr[i]
        for j in range(len(name_arr)):
            print(i, name_arr[j])

