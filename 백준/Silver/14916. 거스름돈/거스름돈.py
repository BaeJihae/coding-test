n = int(input())

m = n // 5
answer = 0

while m >= 0:
    new_n = n - (m*5)
    if new_n % 2 == 0 :
        answer = m + new_n // 2
        break
    else :
        m -= 1

if answer == 0:
    print(-1)
else:
    print(answer)