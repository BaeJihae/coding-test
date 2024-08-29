N = int(input())
lst = list(map(int, input().split()))

M = max(lst)
score_sum = sum(score / M * 100 for score in lst)
print(score_sum/N)