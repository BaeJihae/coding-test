n = int(input())

num_list = list(map(int, input().split()))

k = int(input())

answer = 0

for i in num_list:
    if i == k:
        answer += 1
        
print(answer)