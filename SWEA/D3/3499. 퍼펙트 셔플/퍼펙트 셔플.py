for tc in range(1, int(input()) + 1):
    # 입력
    N = int(input())
    card = input().split()
    deck = [0] * N

    d = (N + 1) // 2

    i1 = 0
    i2 = d
    i3 = 0
    while i3 < N:
        if i1 < d:
            deck[i3] = card[i1]
            i1 += 1
            i3 += 1

        if i2 < N:
            deck[i3] = card[i2]
            i2 += 1
            i3 += 1
    print(f'#{tc}', *deck)