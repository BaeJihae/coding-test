# 공과 잡초

for tc in range(1, int(input()) + 1):
    weeds_str = input()
    pre_chr = ''
    answer = 0
    for chr in weeds_str:
        if pre_chr == '(':
            if chr == '|' or chr == ')':
                answer += 1
        if chr == ')':
            if pre_chr == '|':
                answer += 1
        pre_chr = chr
    print(f'#{tc} {answer}')