def sub_set(bits):
    global answer

    if len(bits) == N:
        sum = 0
        for i in range(N):
            if bits[i] == 1:
                sum += lst[i]
        if sum >= B and answer > sum:
            answer = sum
        return

    sub_set(bits + [0])
    sub_set(bits + [1])

for tc in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    answer = float('inf')
    sub_set([])
    print(f'#{tc} {answer - B}')