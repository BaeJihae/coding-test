n = int(input())
cnt_by_size = list(map(int, input().split()))
t, p = map(int, input().split())

answer = 0
for cnt in cnt_by_size:
    answer += cnt // t
    if cnt % t != 0:
        answer += 1
print(answer)

print(n // p, n % p)
