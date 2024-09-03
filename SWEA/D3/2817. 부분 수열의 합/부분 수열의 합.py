def subset(i):
    global answer

    if i == N:
        sum = 0
        for k in range(N):
            if bits[k] == 1:
                sum += A[k]
        if sum == K:
            answer += 1
        return

    bits[i] = 0
    subset(i + 1)

    bits[i] = 1
    subset(i + 1)

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    answer = 0

    bits = [0] * N
    subset(0)
    print(f'#{tc}', answer)