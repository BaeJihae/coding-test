T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    str = input()
    M = N // 4

    str += str[0:M-1]
    answer = []

    for i in range(M):
        for j in range(4):
            password = int(str[(j*M)+i:(j*M)+i+M],16)
            if password not in answer:
                answer.append(password)

    answer.sort(reverse=True)
    print(f'#{tc} {answer[K-1]}')
