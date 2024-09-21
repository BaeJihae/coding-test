n = int(input())
x = 1
answer = 1
while True:
    if x >= n:
        break
    else:
        x += 6 * answer
        answer += 1

print(answer)