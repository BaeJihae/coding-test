import sys

input = lambda: sys.stdin.readline().strip()

n, m = map(int, input().split())

dict_to_name = {}
dict_to_num = {}
for i in range(1, n + 1):
    name = input()
    dict_to_name[i] = name
    dict_to_num[name] = i

for j in range(m):
    quiz = input()
    if quiz.isdigit():
        print(dict_to_name[int(quiz)])
    else:
        print(dict_to_num[quiz])