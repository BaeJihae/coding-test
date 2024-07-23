import sys

input()
num_list = list(map(int, sys.stdin.readline().split()))

answer = []

num_dict = {}

for index, data in enumerate(sorted(list(set(num_list)))):
    num_dict[data] = index

for i in num_list:
    answer.append(num_dict[i])

for a in answer:
    print(a, end=' ')