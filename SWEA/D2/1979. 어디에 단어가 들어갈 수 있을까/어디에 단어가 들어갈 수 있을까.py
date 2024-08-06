def cnt_word_puzzle(puzzles):
    cnt = 0
    for puzzle in puzzles:
        stack = []
        for p in puzzle:
            if p == 1:
                stack.append(1)
            else:
                if len(stack) == K:
                    cnt += 1
                stack = []
        if len(stack) == K:
            cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    puzzles = [ list(map(int, input().split())) for _ in range(N) ]
    answer = cnt_word_puzzle(puzzles) + cnt_word_puzzle(list(zip(*puzzles)))
    print(f'#{tc} {answer}')
