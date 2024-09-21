n = int(input())

# 자릿수 알아내기
cnt = 0
a = n
while a > 0:
    a = a // 10
    cnt += 1

y = cnt * 9
is_true = False
for x in range(y, cnt * 1 - 1, -1):
    init = n - x
    sum_init = init
    while init > 0:
        sum_init += init % 10
        init //= 10

    if sum_init == n:
        print(n-x)
        is_true = True
        break

if not is_true:
    print(0)